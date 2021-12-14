Rails.application.routes.draw do
  root "actors#index"

  resources :actors
  resources :locations do
    resources :events
  end
end
