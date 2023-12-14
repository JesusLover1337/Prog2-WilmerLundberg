class Brush {
  constructor(ctx, size, color) {
    this.ctx = ctx;
  }
}
class RoundBrush extends Brush {
  constructor(ctx, size, color) {
    super(ctx, size, color);
    this.ctx.lineJoin = "round";
    this.ctx.lineCap = "round";
    this.ctx.lineWidth = size;
    this.ctx.strokeStyle = color;
  }

  startDrawing(x, y) {
    this.ctx.beginPath();
    this.ctx.moveTo(x, y);
  }

  draw(x, y) {
    this.ctx.lineTo(x, y);
    this.ctx.stroke();
  }
}
class RectBrush extends Brush {
  constructor(ctx, size, color) {
    super(ctx, size, color);
    this.ctx.lineJoin = "bevel";
    this.ctx.lineCap = "butt";
    this.ctx.lineWidth = size;
    this.ctx.strokeStyle = color;
  }

  startDrawing(x, y) {
    this.ctx.beginPath();
    this.ctx.moveTo(x, y);
  }

  draw(x, y) {
    this.ctx.lineTo(x, y);
    this.ctx.stroke();
  }
}
const canvas = document.getElementById("drawingCanvas");
const ctx = canvas.getContext("2d");

document.addEventListener("DOMContentLoaded", () => {
  let currentBrush;

  function setBrush(brushType, size, color) {
    if (brushType === "RoundBrush") {
      currentBrush = new RoundBrush(ctx, size, color);
    } else if (brushType === "RectBrush") {
      currentBrush = new RectBrush(ctx, size, color);
    } else if (brushType === null) {
      currentBrush.ctx.lineWidth = size;
    }
    if (brushType === null && size === null) {
      currentBrush.ctx.strokeStyle = color;
    }
  }
  setBrush("RoundBrush", 8, "black");

  let isDrawing = false;

  function startDrawing(event) {
    isDrawing = true;
    const { offsetX, offsetY } = event;
    currentBrush.startDrawing(offsetX, offsetY);
  }

  function draw(event) {
    if (!isDrawing) return;
    const { offsetX, offsetY } = event;
    currentBrush.draw(offsetX, offsetY);
  }

  function stopDrawing() {
    isDrawing = false;
  }

  const brushSelector = document.getElementById("brushSelector");
  brushSelector.addEventListener("change", (e) => {
    const selectedBrush = e.target.value;
    setBrush(selectedBrush, null, null);
  });

  var slider = document.getElementById("numberSlider");
  slider.addEventListener("change", (e) => {
    const size = e.target.value;
    setBrush(null, parseInt(size), null);
  });

  const colorPicker = document.getElementById("colorPicker");
  colorPicker.addEventListener("change", (e) => {
    color = e.target.value;
    setBrush(null, null, color);
  });

  canvas.addEventListener("mousedown", startDrawing);
  canvas.addEventListener("mousemove", draw);
  canvas.addEventListener("mouseup", stopDrawing);
  canvas.addEventListener("mouseout", stopDrawing);
});

function clearArea() {
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}
