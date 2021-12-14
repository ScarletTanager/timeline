class EventsController < ApplicationController
  def index
    #@events = Event.all
    render json: Event.all
  end

  def show
    #@event = Event.find(params[:id])
    render json: Event.find(params[:id])
  end

  def new
    @event = Event.new
  end

  def create
    @location = Location.find(params[:location_id])
    @event = @location.events.create(event_params)

    redirect_to location_path(@location)
  end

  def edit
    @event = Event.find(params[:id])
  end

  def update
    @event = Event.find(params[:id])

    if @event.update(event_params)
      redirect_to @event
    else
      render :edit
    end
  end

  def destroy
    @event = Event.find(params[:id])
    @event.destroy

    redirect_to events_path
  end

  private
    def event_params
      params.require(:event).permit(:name, :short_description, :description)
    end
end
