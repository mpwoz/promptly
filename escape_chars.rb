
# Read escape characters from a file
# returns [escape_sequence, description] pair
def get_escape_chars
  path = "./data/escape_sequences.txt"
  f = File.new(path, "r")
  res = {}
  while (line = f.gets)
    line = line.strip()
    esc, desc = line.split(' ', 2) # Separate on first whitespace
    res[esc] = desc
  end
  return res
end

def get_descriptions
  return get_escape_chars().map { |esc,desc| desc }
end

# Converts a description to an actual escape sequence
def desc_to_esc(desc)
  esc,_ = get_escape_chars().find { |e,d| d==desc }
  return esc
end



