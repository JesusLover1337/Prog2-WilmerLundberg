const canvas = document.getElementById("box");
const ctx = canvas.getContext("2d");
const canvas_width = (canvas.width = 900);
const canvas_height = (canvas.height = 650);

class SpriteSheet {
  constructor(imgPath, width, height) {
    this.imgPath = imgPath;
    this.width = width;
    this.height = height;
  }

  load() {}

  draw(context, x, y) {}
}

class CharacterSpriteSheet extends SpriteSheet {
  constructor(imgPath, width, height, numberOfFrames) {
    super(imgPath, width, height);
    this.numberOfFrames = numberOfFrames;
  }

  animate() {}
}
