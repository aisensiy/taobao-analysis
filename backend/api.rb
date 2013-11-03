require 'grape'
require_relative 'model'
require 'json'

class API < Grape::API
  format :json

  resource :users do
    desc 'Return user list'
    params do
      requires :page, type: Integer
    end
    get do
      users = User.page(params[:page])
      { count: User.cached_count, results: users.to_a }
    end

    desc 'Get single user info'
    params do
      requires :uid, type: Integer
    end
    get ':uid' do
      User.find_by_uid(params[:uid])
    end

    desc 'Return user\'s records'
    params do
      requires :uid, type: String
      requires :page, type: Integer
    end
    route_param :uid do
      get :records do
        records = Record.where(uid: params[:uid]).includes(:urldetail).page(params[:page]).map {|obj| obj.as_json(include: :urldetail) }
        count   = Record.where(uid: params[:uid]).count
        { count: count, results: records }
      end
    end
  end

  resource :sessions do
    desc 'Return a session'
    params do
      require :sessionid, type: Integer
    end
    get ':sessionid' do
      records = Record.where(sessionid: params[:sessionid]).includes(:urldetail).page(params[:page]).map {|obj| obj.as_json(include: :urldetail) }
      count   = Record.where(sessionid: params[:sessionid]).count
      { count: count, results: records }
    end
  end

  resource :urls do
    desc 'Return web content'
    params do
      requires :id, type: Integer
    end
    get ':id' do
      Url.find(params[:id])
    end
  end

end
