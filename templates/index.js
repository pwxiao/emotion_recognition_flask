// 获取 HTML 元素
const input = document.getElementById('function-input');
const button = document.getElementById('draw-button');
const plot = document.getElementById('plot');
let contentsBounds = document.body.getBoundingClientRect();
let width = 800;
let height = 500;
let ratio = contentsBounds.width / width;
width *= ratio;
height *= ratio;
// 绘制函数图像
function drawFunction() {
  // 获取函数表达式
  const expression = input.value;

  // 绘制函数图像
functionPlot({
  target: "#plot",
  width,
  height,
  yAxis: { domain: [-1, 9] },
  grid: true,
  data: [
    {
      fn: expression,
      // derivative: {
      //   fn: "2 * x",
      //   updateOnMouseMove: true
      // }
    }
  ]
});
}

// 添加按钮事件监听器
button.addEventListener('click', drawFunction);