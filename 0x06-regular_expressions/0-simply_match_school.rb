#!/usr/bin/env ruby

def match_school(str)
	regex = /School/
	match = str.match(regex)
	puts match ? match[0] : ""
  end
  
  if ARGV.length != 1
	puts "Usage: #{$PROGRAM_NAME} <string>"
	exit 1
  end
  
  match_school(ARGV[0])
