# **Spike**

## What is Spike?

>Spike is an open source project tackling the national spiking problem within student communities. 

This will be achieved by helping raise awareness of the issue and where reports are being made within your local area. The app is targeted at University Students and should only allow students with .ac email accounts to sign up. By increasing awareness, students can be more cautious in particular areas or venues therefore helping them stay safe.

Students will be able to create an account, view reports, and make reports at local venues. Reports can be displayed in various formats from charts to maps. The aim of the project is to make this information as user friendly and accessible as possible therefore ensuring students are well informed.

There are many issues which must be addressed to make this project successful. One such issue is deciding whether to trust users or whether to have validation for each report. Many of these issues should be carefully considered and discussed among developers therefore we are open to any criticism and believe it is required to create a successful project.

As this project is only in its early development stages, we would encourage all developers to lend a hand and help make this project come to life. Any help that can be provided is much appreciated.

## What have we done so far
Currently, the project is focusing only on Clubs and Pubs within Durham. This helpes remove some complexities to ensure the website is fully functional before expanding to more areas. Below is a list of progress we have made so far:

>- Developed a basic front end using Svelte Kit
>- Created two ways of viewing reports: A heatmap generated using the Google Maps API and a basic reports page displaying severity levels and a total number of reports for each venue
>- Developed a basic backend using Flask. This is almost ready to be deployed

## Our current goals
We have outlined three short terms goals for the project as stated below:
>- Improve the user interface for the webiste to make it more user friendly and *sleek*
>- Add additional ways for students to view reports and monitor local venues by adding notifications or text alerts etc.
>- Add endpoints to the API to allow communication with the front end. The backend should store users, reports, and local venues.

## How can you help?

Know how to code using Svelte or Flask? 
>You could help us out by answering raised issues, fixing bugs in the code, adding additional features, or even commenting the code for other developers.

If the above isn't applicable there is still plenty you could do to help:
>Help remove duplicate issues, add to the repositorys documentation, find out what our target audience would like to see, or test the code for bugs

## Getting started

The project currently uses Svelte Kit for the front end and Flask for the backend. I have included a basic setup guide below for new developers.

<img width="460" src="https://miro.medium.com/max/1400/1*D4Q_5erHUdm8zXNaxPsEGQ.png">

### Using Svelte Kit
To begin, fork this repository and clone it to your personal computer. If your haven't already you must download NodeJS. This can be done using the link provided below:

[Download NodeJS here](https://nodejs.org/en/)

Once cloned, open a terminal and navigate to the directory of the repository. Once inside the directory, navigate to the frontEnd folder and type the code below to start the node server.

<pre>
npm run dev
</pre>

You can now view the front end by opening your browser and typing 'localhost:3000' into the search bar. You can begin edditing the source code by navigating to:

>repository/directory/frontEnd/src/...

If you are new to svelte and would like to learn more, follow the link below to read the documentation and follow the developers handy set of tutorials.

[Svelte Tutorials](https://svelte.dev/tutorial/basics)

### Using Flask