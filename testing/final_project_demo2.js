const params = {"v_input": [1, 0], "m1": [[0.5, 0.5], [0.5, 0.5]], "b1": [0, 0], "m2": [[0.8, 0.4]], "b2": -0.3};

const intermediates = {"v2": [-1, -1], "v3": [-1, -1], "v4": -1, "v5": -1};

// from stack overflow https://stackoverflow.com/questions/808826/draw-arrow-on-canvas-tag
function canvas_arrow(context, fromx, fromy, tox, toy) {
  var headlen = 10; // length of head in pixels
  var dx = tox - fromx;
  var dy = toy - fromy;
  var angle = Math.atan2(dy, dx);
  context.moveTo(fromx, fromy);
  context.lineTo(tox, toy);
  context.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
  context.moveTo(tox, toy);
  context.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
}

function compute_intermediate_values(){
	intermediates["v2"][0] = params["m1"][0][0] * params["v_input"][0] + params["m1"][0][1] * params["v_input"][1] + params["b1"][0];
	intermediates["v2"][1] = params["m1"][1][0] * params["v_input"][0] + params["m1"][1][1] * params["v_input"][1] + params["b1"][1];
	intermediates["v3"][0] = (intermediates["v2"][0] > 0.0 ? intermediates["v2"][0] : 0.0);
	intermediates["v3"][1] = (intermediates["v2"][1] > 0.0 ? intermediates["v2"][1] : 0.0);
	intermediates["v4"] = params["m2"][0][0] * intermediates["v3"][0] + params["m2"][0][1] * intermediates["v3"][1] + params["b2"];
	intermediates["v5"] = (intermediates["v4"] >= 0.5 ? 1.0 : 0.0);
}

function customround(x){
	return (Math.round(x * 100) / 100);
}

function load_text_on_canvas(){
	const canvas = document.getElementById("neuralNetworkGraph");
	const multi = (window.innerWidth >= 900 ? 3 : 1.3);
	if(canvas.getContext){
		const ctx = canvas.getContext("2d");
		ctx.font = "12px Arial";
		ctx.textAlign = "center"
		ctx.fillStyle = "rgba(255, 255, 255, 1)";
		ctx.textBaseline = "middle";
		ctx.fillText("1", multi * 25 + 30, 25);
		ctx.fillText("1", multi * 150 + 30, 25);
		ctx.fillText(customround(params["v_input"][0]), multi * 25 + 30, 100);
		ctx.fillText(customround(params["v_input"][1]), multi * 25 + 30, 200);
		ctx.fillText(customround(intermediates["v2"][0]), multi * 150 - 30, 100);
		ctx.fillText(customround(intermediates["v2"][1]), multi * 150 - 30, 200);
		ctx.fillText(customround(intermediates["v3"][0]), multi * 150 + 30, 100);
		ctx.fillText(customround(intermediates["v3"][1]), multi * 150 + 30, 200);
		ctx.fillText(customround(intermediates["v4"]), multi * 275 - 60, 150);
		ctx.fillText(customround(intermediates["v5"]), multi * 275, 150);
		ctx.fillStyle = "rgba(0, 0, 0, 1)";
		ctx.font = "24px Arial";
		ctx.fillText("v₁", multi * 25 + 30, 275);
		ctx.fillText("v₂", multi * 150 - 30, 275);
		ctx.fillText("v₃", multi * 150 + 30, 275);
		ctx.fillText("v₄", multi * 275 - 60, 275);
		ctx.fillText("v₅", multi * 275, 275);
		ctx.font = "12px Arial";
		ctx.fillText("f", multi * 150, 90);
		ctx.fillText("f", multi * 150, 210);
		ctx.fillText("g", multi * 275 - 30, 140);
		// arrows
		ctx.beginPath();
		canvas_arrow(ctx, multi * 25 + 45, 25, multi * 150 - 45, 100);
		canvas_arrow(ctx, multi * 25 + 45, 25, multi * 150 - 45, 200);
		canvas_arrow(ctx, multi * 25 + 45, 100, multi * 150 - 45, 100);
		canvas_arrow(ctx, multi * 25 + 45, 100, multi * 150 - 45, 200);
		canvas_arrow(ctx, multi * 25 + 45, 200, multi * 150 - 45, 100);
		canvas_arrow(ctx, multi * 25 + 45, 200, multi * 150 - 45, 200);
		canvas_arrow(ctx, multi * 25 + 45, 100, multi * 150 - 45, 100);
		canvas_arrow(ctx, multi * 150 - 15, 100, multi * 150 + 15, 100);
		canvas_arrow(ctx, multi * 150 - 15, 200, multi * 150 + 15, 200);
		canvas_arrow(ctx, multi * 150 + 45, 25, multi * 275 - 75, 150);
		canvas_arrow(ctx, multi * 150 + 45, 100, multi * 275 - 75, 150);
		canvas_arrow(ctx, multi * 150 + 45, 200, multi * 275 - 75, 150);
		canvas_arrow(ctx, multi * 275 - 45, 150, multi * 275 - 15, 150);
		ctx.strokeStyle = "rgba(0, 0, 0, 1)";
		ctx.stroke();
		// weights text
		ctx.font = "12px Arial";
		ctx.fillStyle = "rgba(0, 0, 0, 1)";
		ctx.textAlign = "left";
		ctx.fillText("×" + customround(params["b1"][0]), multi * 25 + 81, 28);
		ctx.fillText("×" + customround(params["b1"][1]), multi * 25 + 81, 70);
		ctx.fillText("×" + customround(params["m1"][0][0]), multi * 25 + 81, 90);
		ctx.fillText("×" + customround(params["m1"][1][0]), multi * 25 + 81, 132);
		ctx.fillText("×" + customround(params["m1"][0][1]), multi * 25 + 81, 168);
		ctx.fillText("×" + customround(params["m1"][1][1]), multi * 25 + 81, 212);
		ctx.fillText("×" + customround(params["b2"]), multi * 150 + 51, 24);
		ctx.fillText("×" + customround(params["m2"][0][0]), multi * 150 + 51, 95);
		ctx.fillText("×" + customround(params["m2"][0][1]), multi * 150 + 51, 207);
	}
	const responsive = (window.innerWidth < 600);
	const tString1 = `\$\$\\text{Inputs: }\\vec{v_1} = \\begin{bmatrix}${params["v_input"][0]}\\\\${params["v_input"][1]}\\end{bmatrix}, W_1 = \\begin{bmatrix}${params["m1"][0][0]} && ${params["m1"][0][1]} \\\\ ${params["m1"][1][0]} && ${params["m1"][1][1]} \\end{bmatrix}, \\vec{b_1} = \\begin{bmatrix}${params["b1"][0]}\\\\${params["b1"][1]}\\end{bmatrix}, W_2 = \\begin{bmatrix}${params["m2"][0][0]} && ${params["m2"][0][1]} \\end{bmatrix}, \\vec{b_2} = \\begin{bmatrix}${params["b2"]}\\end{bmatrix}\$\$`;
	const tStringM1 = `\$\$\\text{Inputs: }\\vec{v_1} = \\begin{bmatrix}${params["v_input"][0]}\\\\${params["v_input"][1]}\\end{bmatrix}, W_1 = \\begin{bmatrix}${params["m1"][0][0]} && ${params["m1"][0][1]} \\\\ ${params["m1"][1][0]} && ${params["m1"][1][1]} \\end{bmatrix}\$\$`
	const tStringM2 = `\$\$\\vec{b_1} = \\begin{bmatrix}${params["b1"][0]}\\\\${params["b1"][1]}\\end{bmatrix}, W_2 = \\begin{bmatrix}${params["m2"][0][0]} && ${params["m2"][0][1]} \\end{bmatrix}, \\vec{b_2} = \\begin{bmatrix}${params["b2"]}\\end{bmatrix}\$\$`;
	const im0 = `\\text{Computed Values: }\\vec{v_2} = W_1\\vec{v_1}+\\vec{b_1} = \\begin{bmatrix}${customround(intermediates["v2"][0])}\\\\${customround(intermediates["v2"][1])}\\end{bmatrix}`;
	const im1 = `\\vec{v_3} = f(\\vec{v_2}) = \\begin{bmatrix}${customround(intermediates["v3"][0])}\\\\${customround(intermediates["v3"][0])}\\end{bmatrix}`;
	const im2 = `\\vec{v_4} = W_2\\vec{v_3}+\\vec{b_2} = \\begin{bmatrix}${customround(intermediates["v4"])}\\end{bmatrix}`;
	const im3 = `\\vec{v_5} = g(\\vec{v_4}) = \\begin{bmatrix}${customround(intermediates["v5"])}\\end{bmatrix}`;
	
	if(responsive){
		document.getElementById("expression").innerText = tStringM1;
		document.getElementById("expressionm").innerText = tStringM2;
		document.getElementById("im0").innerText = "\$\$" + im0 + "\$\$";
		document.getElementById("im1").innerText = "\$\$" + im1 + "\$\$";
		document.getElementById("im2").innerText = "\$\$" + im2 + "\$\$";
		document.getElementById("im3").innerText = "\$\$" + im3 + "\$\$";
	} else {
		document.getElementById("expression").innerText = tString1;
		document.getElementById("expressionm").innerText = "";
		document.getElementById("im0").innerText = "\$\$" + im0 + ", " + im1 + "\$\$";
		document.getElementById("im1").innerText = "\$\$" + im2 + ", " + im3 + "\$\$";
		document.getElementById("im2").innerText = "";
		document.getElementById("im3").innerText = "";
	}
	MathJax.typeset();
}

function draw_network(){
  compute_intermediate_values();
  const canvas = document.getElementById("neuralNetworkGraph");
  const width = window.innerWidth;
  canvas.width = (width >= 900 ? 900 : 390);
  const multi = (width >= 900 ? 3 : 1.3);
  if (canvas.getContext) {
	const ctx9 = canvas.getContext("2d");
	ctx9.beginPath();
	ctx9.roundRect(multi * 25 - 20, 5, 100, 290, 10);
	ctx9.stroke();
	ctx9.fillStyle = "rgba(208, 68, 73, 0.5)";
	ctx9.fill();
	const ctx10 = canvas.getContext("2d");
	ctx10.beginPath();
	ctx10.roundRect(multi * 275 - 80, 5, 100, 290, 10);
	ctx10.stroke();
	ctx10.fillStyle = "rgba(66, 135, 245, 0.5)";
	ctx10.fill();
	const ctx11 = canvas.getContext("2d");
	ctx11.beginPath();
	ctx11.roundRect(multi * 150 - 50, 5, 100, 290, 10);
	ctx11.stroke();
	ctx11.fillStyle = "rgba(64, 199, 77, 0.5)";
	ctx11.fill();
    const ctx1 = canvas.getContext("2d");
	const ctx2 = canvas.getContext("2d");
    ctx1.beginPath();
    ctx1.arc(multi * 25 + 30, 100, 15, 0, 2 * Math.PI);
	ctx1.stroke();
	ctx1.fillStyle = "rgba(208, 68, 73, 1)";
	ctx1.fill();
	ctx2.beginPath();
	ctx2.arc(multi * 25 + 30, 200, 15, 0, 2 * Math.PI);
	ctx2.stroke();
	ctx2.fillStyle = "rgba(208, 68, 73, 1)";
	ctx2.fill();
	const ctx3 = canvas.getContext("2d");
	const ctx4 = canvas.getContext("2d");
	ctx3.beginPath();
    ctx3.arc(multi * 150 - 30, 100, 15, 0, 2 * Math.PI);
	ctx3.stroke();
	ctx3.fillStyle = "rgba(64, 199, 77, 1)";
	ctx3.fill();
	ctx4.beginPath();
	ctx4.arc(multi * 150 - 30, 200, 15, 0, 2 * Math.PI);
	ctx4.stroke();
	ctx4.fillStyle = "rgba(64, 199, 77, 1)";
	ctx4.fill();
	const ctx5 = canvas.getContext("2d");
	const ctx6 = canvas.getContext("2d");
	ctx5.beginPath();
    ctx5.arc(multi * 150 + 30, 100, 15, 0, 2 * Math.PI);
	ctx5.stroke();
	ctx5.fillStyle = "rgba(64, 199, 77, 1)";
	ctx5.fill();
	ctx6.beginPath();
	ctx6.arc(multi * 150 + 30, 200, 15, 0, 2 * Math.PI);
	ctx6.stroke();
	ctx6.fillStyle = "rgba(64, 199, 77, 1)";
	ctx6.fill();
	const ctx7 = canvas.getContext("2d");
    ctx7.beginPath();
    ctx7.arc(multi * 275 - 60, 150, 15, 0, 2 * Math.PI);
	ctx7.stroke();
	ctx7.fillStyle = "rgba(66, 135, 245, 1)";
	ctx7.fill();
	const ctx8 = canvas.getContext("2d");
    ctx8.beginPath();
    ctx8.arc(multi * 275, 150, 15, 0, 2 * Math.PI);
	ctx8.stroke();
	ctx8.fillStyle = "rgba(66, 135, 245, 1)";
	ctx8.fill();
	const ctxa1 = canvas.getContext("2d");
	ctxa1.beginPath();
	ctxa1.arc(multi * 25 + 30, 25, 15, 0, 2 * Math.PI);
	ctxa1.stroke();
	ctxa1.fillStyle = "rgba(64, 64, 64, 1)";
	ctxa1.fill();
	ctxa1.beginPath();
	ctxa1.arc(multi * 150 + 30, 25, 15, 0, 2 * Math.PI);
	ctxa1.stroke();
	ctxa1.fillStyle = "rgba(64, 64, 64, 1)";
	ctxa1.fill();
	load_text_on_canvas();
  }
}

window.onload = (event) => {
  console.log("page is fully loaded");
  draw_network();
  console.log(window.innerWidth);
  if(window.innerWidth < 600){
	  console.log("aidsninda");
	  document.getElementById("pcver1").innerText = "$$\\text{Activation Function: } f(x) = \\begin{cases} x \\text{ if } x \\ge 0 \\\\ 0 \\text { if } x \\lt 0 \\end{cases}$$";
	  document.getElementById("mobileonly1").innerText = "$$\\text{Output Function: } g(x) = \\begin{cases} 1 \\text{ if } x \\ge 0.5 \\\\ 0 \\text{ if } x \\lt 0.5 \\end{cases}$$";
	  MathJax.typeset();
  }
};
//document.write("Hello world!");

function update(){
	console.log("H");
	const mappings = [
		// param name, index 0, index 1, id
		["v_input", 0, -1, "vinput1"],
		["v_input", 1, -1, "vinput2"],
		["m1", 0, 0, "w111"],
		["m1", 0, 1, "w112"],
		["m1", 1, 0, "w121"],
		["m1", 1, 1, "w122"],
		["b1", 0, -1, "b11"],
		["b1", 1, -1, "b12"],
		["m2", 0, 0, "w211"],
		["m2", 0, 1, "w212"],
		["b2", -1, -1, "b21"]
	];
	mappings.forEach((mapping) => {
		const target_element = document.getElementById(mapping[3]);
		targetValue = parseFloat(target_element.value);
		if(!isNaN(targetValue)){
			console.log(targetValue);
			if(mapping[1] == -1){
				params[mapping[0]] = customround(targetValue);
			} else if (mapping[2] == -1){
				params[mapping[0]][mapping[1]] = customround(targetValue);
			} else {
				params[mapping[0]][mapping[1]][mapping[2]] = customround(targetValue);
			}
		}
		let param_element = params[mapping[0]];
		if(mapping[1] != -1){
			param_element = param_element[mapping[1]];
		}
		if(mapping[2] != -1){
			param_element = param_element[mapping[2]];
		}
		target_element.value = param_element;
	});
	draw_network();
}
