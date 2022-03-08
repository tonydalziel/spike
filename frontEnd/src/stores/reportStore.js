import {writable} from "svelte/store";

export const tempReports = writable([]);

const fetchReports = async () => {
    const res = await fetch('http://127.0.0.1:8090/basicReports');
    const data = await res.json();
    if(data != tempReports){
        data.sort((a,b)=> b.severity - a.severity);
        tempReports.set(data);
    }
};
fetchReports();
setInterval(() => {
    fetchReports();
}, 10000);