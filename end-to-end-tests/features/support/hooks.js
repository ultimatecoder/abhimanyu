//const { webdriver } = require('selenium-webdriver');
let webdriver = require('selenium-webdriver');
const { Before, After} = require('cucumber');
let driver = require('../selenium_instance');

Before(function() {
  driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.firefox()).build();
})

After(function() {
  driver.quite();
})
