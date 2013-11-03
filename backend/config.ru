$:.unshift File.expand_path("../", __FILE__)

require 'api'
require 'rack/cors'

use Rack::Cors do
    allow do
      origins '*'
      # location of your API
      resource '*', :headers => :any, :methods => [:get, :post, :options, :put]
    end
end

run API
