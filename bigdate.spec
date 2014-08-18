# BigDate specification file
# Created with sur-0.2.143
Sur::Specification.new do |s|
  s.name        = "BigDate"
  s.authors     = [ "0rax" ]
  s.contact     = "roemer.jp@gmail.com"
  s.date        = "Mon Aug 18 01:30:22 2014"
  s.description = "Display date and time with a big clock icon"
  s.notes       = <<NOTES
This sublet is here to replace clock for people having HDPI screen like me, shipped with a 20x20 icon.
You can add text before and after using 'prefix' and 'suffix' and hide icon using 'show_icon'.
Change how the date is shown using 'format'
NOTES
  s.config = [
    {
  	:name        => "prefix",
  	:type        => "string",
  	:description => "Prefix",
  	:def_value   => " "
    },
    {
  	:name        => "suffix",
  	:type        => "string",
  	:description => "Suffix",
  	:def_value   => ""
    },
    {
  	:name        => "show_icon",
  	:type        => "bool",
  	:description => "Show icon",
  	:def_value   => true
    },
    {
  	:name        => "format",
  	:type        => "string",
  	:description => "date format string",
  	:def_value   => "%H:%M %d/%m/%y"
    }
  ]
  s.version     = "0.1"
  s.tags        = [ "Clock", "BigIcon", "Date" ]
  s.files       = [ "bigdate.rb" ]
  s.icons       = [ "clock.xbm" ]
end
