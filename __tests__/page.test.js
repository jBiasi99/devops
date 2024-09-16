const puppeteer = require('puppeteer');

test('A página deve carregar corretamente', async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:8080');
  const title = await page.title();
  expect(title).not.toBeNull();
  await browser.close();
});
