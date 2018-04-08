function createTimeline () {
  var timeline = {
    startDate: 0,
    endDate: 0,
    events: []
  };
  var my_canvas = document.getElementById('mycanvas');
  var context = my_canvas.getContext('2d');
  console.log("Clearing canvas");
  context.clearRect(0, 0, my_canvas.width, my_canvas.height);

  context.strokeStyle = "#000000";
  var dateFont = "12px Arial";
  var eventFont = "15px Arial";

  var startX = 50;
  var endX = 950;
  var startY = 200;
  var dateY = 225;

  console.log("drawing timeline");
  context.beginPath();
  context.moveTo(startX,startY);
  context.lineTo(endX,startY);
  context.stroke();
  context.closePath();

  drawDateHashes(context, startX, endX, startY, dateY);
}

function drawDateHashes (ctx, startX, endX, startY, dateY) {
  var startDate = getStartDate();
  var endDate = getEndDate();
  var interval = getDateInterval();
  var lineLength = endX - startX;
  var duration = endDate.diff(startDate);

  // Draw beginning and ending hashes
  drawDateHash(ctx, startX, startY, dateY, startDate);
  drawDateHash(ctx, endX, startY, dateY, endDate);

  // Draw the interval hashes
  var intervalDate = moment(startDate);
  while(intervalDate.add(interval, 'y').isBefore(endDate)) {
    var xOffset = getTimelineOffset(lineLength, duration, startDate, intervalDate);
    console.log("Setting interval hash at " + intervalDate.format("M-D-Y") + " with offset " + xOffset);
    var intervalX = startX + xOffset;
    console.log("Drawing interval hash from " + intervalX
    + "," + startY + " to " + intervalX + "," + dateY);
    drawDateHash(ctx, intervalX, startY, dateY, intervalDate);
  }
}

// Find the correct X offset for date d on the timeline
// len is the length in pixels of the timeline
// span is the timespan of the timeline in milliseconds
// s is the moment representation of the timeline start date
// d is a moment represention of the event date
function getTimelineOffset(len, span, s, d) {
  if (d.isBefore(s)) {
    console.log("Bad event date");
    return 0;
  }

  console.log("Computing offset with len: " + len + "; span: " + span
    + "; startDate: " + s.format("M-D-Y") + "; eventDate: " + d.format("M-D-Y"));
  var t = Math.abs(s.diff(d));
  var offset = Math.trunc((t/Math.abs(span)) * Math.abs(len));
  console.log("X offset computed as " + offset);
  return offset;
}

function drawDateHash (ctx, x, startY, endY, date) {
  console.log("Drawing from " + x + "," + startY + " to " + x + "," + endY);
  ctx.beginPath();
  ctx.moveTo(x, startY);
  ctx.lineTo(x, endY);
  ctx.stroke();
  ctx.textAlign = "center";
  ctx.fillText(date.format("M-D-Y"), x, endY + 25);
}

function getStartDate () {
  var startDate = moment([
    document.getElementById('startMonth').value,
    document.getElementById('startDay').value,
    document.getElementById('startYear').value].join("-"), "M-D-Y");
  return startDate;
}

function getEndDate () {
    var endDate = moment([
      document.getElementById('endMonth').value,
      document.getElementById('endDay').value,
      document.getElementById('endYear').value].join("-"), "M-D-Y");
  return endDate;
}

function getDateInterval () {
  var interval = document.getElementById('interval').value;
  return interval;
}

function addTimelineEvent () {
  var my_canvas = document.getElementById('mycanvas');
  var ctx = my_canvas.getContext('2d');

  ctx.strokeStyle = "#000000";
  var dateFont = "12px Arial";
  var eventFont = "15px Arial";

  var eventDate = getEventDate();
  var eventName = getEventName();
  var startDate = getStartDate();
  var endDate = getEndDate();

  var startX = 50;
  var endX = 950;
  var startY = 200;
  var eventY = 175;

  var eventX = startX + getTimelineOffset((endX - startX), startDate.diff(endDate), startDate, eventDate);
  ctx.beginPath();
  ctx.moveTo(eventX, startY);
  ctx.lineTo(eventX, eventY);
  ctx.stroke();
  ctx.textAlign = "center";
  ctx.fillText(eventName, eventX, eventY - 25);
}

function getEventDate () {
  var eventDate = moment([
    document.getElementById('eventMonth').value,
    document.getElementById('eventDay').value,
    document.getElementById('eventYear').value].join("-"), "M-D-Y");
  return eventDate;
}

function getEventName () {
  var eventName = document.getElementById('eventName').value;
  return eventName;
}
