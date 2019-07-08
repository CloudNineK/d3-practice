let width = 800, height = 800;

let svg = d3.select('body')
  .append('svg')
  .attr('width', width)
  .attr('height', height)

let g = svg.append('g');

let proj = d3.geoAlbersUsa();

g.selectAll('path')
  .data(neighborhoods.features)
  .enter()
  .append('path')
  .attr('fill', 'blue')
  .attr('d', proj)