#!/usr/bin/node

const redHeader = $('DIV#red_header');
redHeader.on('click', () => {
  const header = $('header');
  header.css('color', '#FF0000');
});
