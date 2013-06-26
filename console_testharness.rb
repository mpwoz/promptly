require_relative 'escape_chars'


puts "Which escape seq?"
descs = get_descriptions()
descs.each_with_index { |d,i| puts i.to_s + " ... " + d }

choice = gets

puts desc_to_esc(descs[choice.to_i])
