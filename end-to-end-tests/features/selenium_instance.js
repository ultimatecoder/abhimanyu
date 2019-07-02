let webdriver = require('selenium-webdriver');
let driver;

declareDriver = function() {
  driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.firefox()).build();
}

quiteDriver = function() {
  driver.quite();
}

module.exports = {
  declareDriver: declareDriver,
  quiteDriver: quiteDriver,
  driver: driver
};

//export { declareDriver, quiteDriver };

//export { driver }

//export let driver = 4;
