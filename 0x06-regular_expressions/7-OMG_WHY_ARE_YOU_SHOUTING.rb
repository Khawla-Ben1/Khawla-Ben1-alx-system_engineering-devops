#!/usr/bin/env ruby
pattern = /[A-Z]/
input = ARGV[0]

matches = input.scan(pattern)
result = matches.join

puts result
