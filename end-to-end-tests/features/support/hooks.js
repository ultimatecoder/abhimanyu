let webdriver = require('selenium-webdriver');
const { Before, After} = require('cucumber');
const { declareDriver, quiteDriver } = require('../selenium_instance');

Before(function() {
  declareDriver();
})

After(function() {
  quiteDriver();
})
