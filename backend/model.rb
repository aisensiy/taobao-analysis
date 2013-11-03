require 'zlib'
require 'active_record'
require 'will_paginate'
require 'will_paginate/active_record'

config = {
  adapter: 'mysql2',
  database: 'spide',
  username: 'kv',
  password: 'kvlab2013',
  host: '162.105.11.56'
}

ActiveRecord::Base.establish_connection(config)
ActiveRecord::Base.logger = Logger.new(STDOUT)
ActiveRecord::Base.include_root_in_json = false

WillPaginate.per_page = 50

class User < ActiveRecord::Base
  self.table_name = 'joined_users_have_records'

  has_many :records, class_name: 'Record', foreign_key: 'uid', primary_key: 'uid'

  def self.cached_count
    @cached_count ||= User.count
  end
end

class Record < ActiveRecord::Base
  self.table_name = 'taobao'

  has_one :urldetail, class_name: 'Url', foreign_key: 'url_md5', primary_key: 'url_md5', select: [:id, :urlpath, :cleanurl, :url_md5, :title]
end

class Url < ActiveRecord::Base
  self.table_name = 'url'

  belongs_to :record, class_name: 'Record', primary_key: 'url_md5', foreign_key: 'url_md5'

  def content
    return if self[:content].nil?
    gz = Zlib::GzipReader.new(StringIO.new(self[:content]))
    gz.read
  end
end
