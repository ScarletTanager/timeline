function createTimeline () {
  var my_canvas = document.getElementById('mycanvas');
  var context = my_canvas.getContext('2d');
  context.clearRect(0, 0, my_canvas.width, my_canvas.height);

  context.strokeStyle = "#000000";
  var dateFont = "12px Arial";
  var eventFont = "15px Arial";

  var startX = 50;
  var endX = 950;
  var startY = 200;
  var dateY = 225;

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
  // Draw beginning and ending hashes
  drawDateHash(ctx, startX, startY, dateY, startDate);
  drawDateHash(ctx, endX, startY, dateY, endDate);

  var lineLength = endX - startX;
  var duration = endDate - startDate;
  var intervalCount = duration / interval;
  var intervalLineLength = Math.trunc(lineLength / intervalCount);
  intervalCount = Math.trunc(intervalCount);

  for (i = 1; i <= intervalCount; i++) {
    drawDateHash(ctx, startX + (i * intervalLineLength), startY, dateY, parseInt(startDate) + (i * interval));
  }
}

function drawDateHash (ctx, x, startY, endY, date) {
  console.log("Drawing from " + x + "," + startY + " to " + x + "," + endY);
  ctx.beginPath();
  ctx.moveTo(x, startY);
  ctx.lineTo(x, endY);
  ctx.stroke();
  ctx.textAlign = "center";
  ctx.fillText(date, x, endY + 25);
}

function getStartDate () {
  var startDate = document.getElementById('startDate').value;
  return startDate;
}

function getEndDate () {
  var endDate = document.getElementById('endDate').value;
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

  var eventX = startX + Math.trunc((eventDate - startDate)/(endDate - startDate) * (endX - startX));
  ctx.beginPath();
  ctx.moveTo(eventX, startY);
  ctx.lineTo(eventX, eventY);
  ctx.stroke();
  ctx.textAlign = "center";
  ctx.fillText(eventName, eventX, eventY - 25);
}

function getEventDate () {
  var eventDate = document.getElementById('eventDate').value;
  return parseInt(eventDate);
}

function getEventName () {
  var eventName = document.getElementById('eventName').value;
  return eventName;
}
