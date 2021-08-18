/* globals gauge*/
"use strict";
const path = require('path');
const {
    openBrowser,
    write,
    closeBrowser,
    goto,
    dropDown,
    press,
    screenshot,
    above,
    click,
    checkBox,
    listItem,
    toLeftOf,
    link,
    text,
    into,
    textBox,
    evaluate
} = require('taiko');
const assert = require("assert");
const headless = process.env.headless_chrome.toLowerCase() === 'true';

let marsAirUrl = "https://marsair.thoughtworks-labs.net/renan.de.paula";

beforeSuite(async () => {
    await openBrowser({
        headless: headless
    })
});

afterSuite(async () => {
    await closeBrowser();
});

// Return a screenshot file name
gauge.customScreenshotWriter = async function () {
    const screenshotFilePath = path.join(process.env['gauge_screenshots_dir'],
        `screenshot-${process.hrtime.bigint()}.png`);

    await screenshot({
        path: screenshotFilePath
    });
    return path.basename(screenshotFilePath);
};


step("Goto MarsAirs homepage", async function () {
    await goto(marsAirUrl);
});


step("Click <button>", async function (button) {
    await click(button);
});

step("Click in <field> and select <option>", async function (field, option) {
    await dropDown(field).select(option);
});

step("Type promotion code <code>", async function (code) {
    await click(textBox('Promotional Code'));
    await write(code);
});

step("Write <text>", async function (text) {
    await write(text);
});

step("Verify if message <message> is displayed", async function (message) {
    assert.ok(await text(message).exists());
});

step("Verify if discount of <discount> from <code> is applied", async function (discount, code) {
    assert.ok(await text(`Promotional code ${code} used: ${discount}% discount!`).exists());
});

step("Verify if discount from <code> is not valid", async function (code) {
    assert.ok(await text(`Sorry, code ${code} is not valid`).exists());
});