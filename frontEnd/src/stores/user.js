import { writable } from "svelte/store";
import {browser} from "$app/env";

export const user = writable(browser && ((localStorage.getItem("user") == null) || (localStorage.getItem("user") == "null")? (localStorage.getItem("user")) : JSON.parse(localStorage.getItem("user"))));

user.subscribe((val) =>browser && localStorage.setItem("user",JSON.stringify(val)));