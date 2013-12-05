#!/usr/bin/env ruby

God.watch do |w|
  w.name = 'taobao-backend'
  w.start = 'unicorn ~/projects/taobao-analysis/backend/config.ru -p9292'
  w.keepalive
end
