<html lang="en">
  <head>
    <meta charset="utf-8">
    <script src="//code.jquery.com/jquery-2.0.0.js"></script>
    <style>
    #map {
      background-color: #fff;
      border: 1px solid #ccc;
    }
    .background {
      fill: #ef;
      pointer-events: all;
    }
    
    pre.prettyprint {
      border: 1px solid #ccc;
      margin-bottom: 0;
      padding: 9.5px;
    }

    .selected {
      fill:yellow;
    }

    #states {
      fill: #cde;
      stroke: #fff;
      stroke-linejoin: round;
      stroke-linecap: round;
    }
    </style>
  


    <title>SVG</title>

    
</head>

<body>
	<div id="map"></div>
	<script src="http://d3js.org/d3.v3.min.js"></script>
    <script src="//d3js.org/topojson.v1.min.js"></script>
	<script>
	
		var margin = { top: 0, left: 0, right: 0, bottom: 0 },
			height  = 600 - margin.top - margin.bottom,
			width = 800 - margin.left - margin.right;
	    
		var svg = d3.select("#map").append("svg")
		    .attr("width", width + margin.left + margin.right)
		    .attr("height", height + margin.top + margin.bottom)
		    .append("g")
		    .attr("transfrom", "translate(" + margin.left + "," + margin.top + ")");

		
		var projection = d3.geo.mercator()  
	       .center([132, -28])  
	       .scale(850)  
	       .translate([width/2, height/2]);

		var path = d3.geo.path()
			.projection(projection)
		
		var states = svg.append("svg:g")  
        	.attr("id", "states");  

    var circles = svg.append("svg:g")  
        .attr("id", "circles");  
  
    var texts = svg.append("svg:g")  
        .attr("id", "texts");  

	

		d3.json("aus.big.cities.json", function(error, root) {  
        circles.selectAll("circle")  
            .data(root.features)  
            .enter().  
            append("svg:circle")  
            .attr("cx", function(d){return projection([d.properties['LONGITUDE'],d.properties['LATITUDE']])[0];})//根据城市的经纬度投射确定圆点坐标  
            .attr("cy",function(d){return projection([d.properties['LONGITUDE'],d.properties['LATITUDE']])[1];})  
            .attr("r", 2.6)  
            


        texts.selectAll("text")  
            .data(root.features)  
            .enter()  
            .append("svg:text")  
            .text(function(d){return d.properties['NAME'];})  
            .attr("x", function(d){  
                return projection([ d.properties['LONGITUDE'],d.properties['LATITUDE']])[0];})  
            .attr("y",function(d){  
                return projection([d.properties['LONGITUDE'],d.properties['LATITUDE']])[1];  
            })  
            .attr('fill','#c')  
            .attr('font-size','7px')
            .attr("dx",5);
        })  

    d3.json("states.json", function(error, data) {
      console.log(data)

          states.selectAll(".path")  
              .data( data.features)  
              .enter()  
              .append("path")
              .attr("class", "states")
              .attr("d", path )
              .on('mouseover', function(d){
                d3.select(this).classed("selected", true)
              })
              .on('mouseout', function(d){
                d3.select(this).classed("selected", false)
              })
              .attr("fill", "#ccc")
              .attr("stroke","#333333")//路径线颜色  
              .attr("stroke-width",0.5)//路径线宽度  
      
        })  
    var route = svg.append("path")
               .datum({type: "LineString", coordinates: [origin, destination]})
               .attr("class", "route")
               .attr("d", path);
			
	</script>
	


</body>

</html>
