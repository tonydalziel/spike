<script>
    //TODO: Ensure only neccessary imports are made
    import { placesKey } from '../stores/apiKey';
    export let reports;
    export let name;
    export let lastReport;
    export let severity;
    export let photoID;
    let imageURL;
    $: hue = (1-severity) * (120);
     'hsl(' + hue + ', 100%, 50%)';
    if(photoID){
        if(photoID == "Default"){
            imageURL = 'https://images.unsplash.com/photo-1633432111221-8b25d9c73c42?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2128&q=80';
        }else{
            imageURL = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photo_reference='+photoID+'&key='+placesKey;
        }
    }else{
        imageURL = 'https://images.unsplash.com/photo-1633432111221-8b25d9c73c42?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2128&q=80';
    }

</script>

<!--Need to fix the way in which the image is displayed on smaller devices-->
<!--Should continuouslly sort data to ensure highest number of incidents shows at the top-->
<div class="p-6 bg-gray-100/50 rounded-md shadow-sm hover:shadow-md flex justify-start flex-wrap md:flex-nowrap">
    <div class="grow mr-2 basis-2 md:basis-3/4">
        <h2 class="font-thin font-sans text-2xl mb-2">{name}</h2>
        <div>
            <h3 class="font-thin font-sans inline">Reports in 48 hours:</h3>
            <h3 class="inline text-lg {reports === 0?'text-black' : 'text-rose-500'}">{reports}</h3>
            <br>
            <p class="font-thin font-sans inline">Last report:</p>
            <h3 class="inline text-lg">{lastReport}</h3>
        </div>
        <div class="flex justify-start items-center h-fit">
            <p class="font-thin font-sans mr-2">Severity:</p>
            <div class="grow bg-white/50 h-4 mt-1">
                <!--Calculate colour and size based off of severity-->
                <div class="h-4" style="width: {100*severity}%; background-color: hsl({hue}, 75%,50%);"></div>
            </div>
        </div>
    </div>
    <div class="grow bg-center bg-cover md:basis-1/4 basis-1 min-w-fit md:min-w-0 mt-3 md:mt-0 bg-white border-2 border-black" style="{imageURL? `background-image: url('${imageURL}')`: ''};">
        <div class="block w-96 h-40 md:h-0"></div>
    </div>
</div>