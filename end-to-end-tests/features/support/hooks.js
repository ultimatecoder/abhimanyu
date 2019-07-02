//const { webdriver } = require('selenium-webdriver');
let webdriver = require('selenium-webdriver');
const { Before, After} = require('cucumber');
const { declareDriver, quiteDriver } = require('../selenium_instance');
//let seleniumInstance = require('../selenium_instance');

Before(function() {
  //driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.firefox()).build();
  //seleniumInstance.declareDriver();
  //console.log(seleniumInstance.declareDriver);
  declareDriver();
})

After(function() {
  quiteDriver();
  //driver.quite();
})
