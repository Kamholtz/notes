---
id: 19d13674-ea71-4431-bb85-e8182f6c8ebf
title: Kendo
desc: ''
updated: 1616465049360
created: 1616464550754
---

## Templates

[Templates Overview | Kendo UI Templates | Kendo UI for jQuery](https://docs.telerik.com/kendo-ui/framework/templates/overview)

### For Loops

[Kendo templates and for loops](https://majorsilence.com/docs/Javascript/kendo-templates-loops)


```html
<div data-bind="source: data" data-template="tmp"></div>
<script id="tmp" type="text/x-kendo-template">
  <div>
    <input data-bind="value: quantity" />
    <span data-bind="text: price"></span>
    <span data-bind="text: total"></span>
     #for (var i=0,len=Accounts.length; i<len; i++){#
            <p>${ Accounts[i] }</p>
     # } #
  </div>
</script>
```