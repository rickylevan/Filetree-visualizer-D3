var fs = require('fs');
var d3 = require('d3');
var xmldom = require('xmldom');

var width = 960,
    height = 2200;

var cluster = d3.layout.cluster()
    .size([height, width - 160]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  	.append("g")
    .attr("transform", "translate(40,0)");

// var root = fs.readFile("/resources/d/flare.json")

fs.readFile('pretty_sample_solved.json', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }

  var root = JSON.parse(data);

  var nodes = cluster.nodes(root),
      links = cluster.links(nodes);


  var link = svg.selectAll(".link")
      .data(links)
      .enter().append("path")
      .attr("class", "link")
      .attr("d", diagonal)
	  .style("fill","none")
			.style("stroke","#ccc")
			.style("stroke-width","1.5px")

  var node = svg.selectAll(".node")
      .data(nodes)
      .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })
	  .style("fill","#fff")
	  .style("stroke","steelblue")
	  .style("stroke-width","1.5px");

  node.append("circle")
      .attr("r", 4.5);


  node.append("text")
      .attr("dx", function(d) { return d.children ? -8 : 8; })
      .attr("dy", 3)
      .style("text-anchor", function(d) { return d.children ? "end" : "start"; })
	  .style("font-family","sans-serif")
	  .style("font-size","10px")
	  .style("stroke","none")
	  .style("fill","black")
	  .style("font-weight","400")
      .text(function(d) { return d.name; });

	// d3.select(self.frameElement).style("height", height + "px");


var svgGraph = d3.select('svg')
	.attr('xmlns', 'http://www.w3.org/2000/svg');
var svgXML = (new xmldom.XMLSerializer()).serializeToString(svgGraph[0][0]);
fs.writeFile('filesys_demo.svg', svgXML); 



});


