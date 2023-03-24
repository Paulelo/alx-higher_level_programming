#!/usr/bin/node
import { argv } from 'node:process';

let x = argv.length()
if (x = 2) {
    console.log("No argument");
    } else if (x = 3) {
    console.log("Argument found");
    } else if (x > 3) {
    console.log("Arguments found");
    }
