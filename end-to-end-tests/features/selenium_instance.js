let webdriver = require('selenium-webdriver');
var driver = "test";

declareDriver = function() {
  driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.firefox()).build();
}

getDriver = function() {
  return driver;
}

quiteDriver = function() {
  driver.quit();
}

module.exports = {
  declareDriver: declareDriver,
  quiteDriver: quiteDriver,
  driver: driver,
  getDriver: getDriver
};
