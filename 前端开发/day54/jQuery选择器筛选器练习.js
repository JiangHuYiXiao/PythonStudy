
//因为html中已经通过CDN引入了jQuery所以这里就不需要再次引入了
/*
找到本页面中id是i1的标签
找到本页面中所有的h2标签
找到本页面中所有的input标签
找到本页面所有样式类中有c1的标签
找到本页面所有样式类中有btn-default的标签
找到本页面所有样式类中有c1的标签和所有h2标签
找到本页面所有样式类中有c1的标签和id是p3的标签
找到本页面所有样式类中有c1的标签和所有样式类中有btn的标签

找到本页面中form标签中的所有input标签
找到本页面中被包裹在label标签内的input标签
找到本页面中紧挨在label标签后面的input标签
找到本页面中id为p2的标签后面所有和它同级的li标签

找到id值为f1的标签内部的第一个input标签
找到id值为my-checkbox的标签内部最后一个input标签
找到id值为my-checkbox的标签内部没有被选中的那个input标签
找到所有含有input标签的label标签
*/
// 1、找到本页面中id是i1的标签
console.log($("#i1"));

// 2、找到本页面中所有的h2标签
console.log($("h2"));

// 3、找到本页面中所有的input标签
console.log($("input"));

// 4、找到本页面所有样式类中有c1的标签
console.log($(".c1"));

// 5、找到本页面所有样式类中有btn-default的标签
console.log($(".btn-default"));

// 6、找到本页面所有样式类中有c1的标签和所有h2标签
console.log($(".c1,h2"));

// 7、找到本页面所有样式类中有c1的标签和id是p3的标签
console.log($(".c1,#p3"));

// 8、找到本页面所有样式类中有c1的标签和所有样式类中有btn的标签
console.log($(".c1,.btn"));

// 9、找到本页面中form标签中的所有input标签
console.log($("form input"));

// 10、找到本页面中被包裹在label标签内的input标签
console.log($("label>input"));

// 11、找到本页面中紧挨在label标签后面的input标签
console.log($("label+input"));

// 12、找到本页面中id为p2的标签后面所有和它同级的li标签
console.log($("#p2~li"));

// 13、找到id值为f1的标签内部的第一个input标签
console.log($("#f1 input:first"));

// 14、找到id值为my-checkbox的标签内部最后一个input标签
console.log($("#my-checkbox input:last"));

// 15、找到id值为my-checkbox的标签内部没有被选中的那个input标签
console.log($("#my-checkbox input:not(:selected)"));

// 16、找到所有含有input标签的label标签
console.log($("label:has(input)"));

