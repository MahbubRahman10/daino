
"use strict";

ckan.module('demo_popover', function ($) {
  return {
    initialize: function () {
      alert("hello")
      console.log("I've been initialized for element: ", this.el);
    }
  };
});
