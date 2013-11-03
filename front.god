#!/usr/bin/env ruby

God.watch do |w|
  w.name = 'taobao-frontend'
  w.start = 'grunt server --gruntfile ~/projects/taobao-analysis/frontend/Gruntfile.js'
  w.keepalive
end
