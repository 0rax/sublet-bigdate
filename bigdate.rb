# BigDate sublet file
# Created with sur-0.1
configure :bigdate do |s| # {{{
  s.interval = s.config[:interval]      || 60
  s.format   = s.config[:format]        || "%H:%M %d/%m/%y"
  s.prefix   = s.config[:prefix]        || " "
  s.suffix   = s.config[:suffix]        || ""
  s.show_icon= s.config[:show_icon]     || true
  s.icon     = Subtlext::Icon.new("clock.xbm")
end # }}}

on :run do |s| # {{{
  if s.show_icon == true
    s.data = s.icon + s.prefix + Time.now().strftime(s.format) + s.suffix
  else
    s.data = s.prefix + Time.now().strftime(s.format) + s.suffix
  end
end # }}}
