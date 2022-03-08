<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    let userName;
    let pass;
    let email;
    let passAgain;
    let submitted = false;
    let errorMessage;

    async function register(event){
      submitted = true;
      let valid = true;
      const formData = new FormData(event.target);
      console.log(formData);
      for ( let field of formData ) {
        const [key, value] = field;
        if(!value || value.replace(/\s/g, "") === "" ) {
            valid = false;
        }
        //Add an additional check here for emails
      }
      if(passAgain !== pass){
        valid = false
      }
      if(valid){
        //Make all of these responses into POST requests once the backend has been setup
        //Should have responses if the emails are already registered or if the username is already in use
        const res = await fetch(`http://127.0.0.1:8090/newUser?username=${userName}&password=${pass}`);
        const data = await res.json();
        if(data.valid){
          dispatch('registered');
        }else{
          errorMessage = data.message;
        }
      }
    }
</script>

<div class="flex justify-center items-center h-screen px-4">
    <div class="grow max-w-xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
        {#if errorMessage && submitted}
          <p class="text-red-500 text-md text-center italic">{errorMessage}</p>
        {/if}
        <form on:submit|preventDefault={register}>
          <div class="mb-4">
            <label class="block text-grey-darker text-sm font-bold mb-2" for="username">
              Username
            </label>
            <input bind:value={userName} class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker mb-3" id="username" name="username" type="text" placeholder="Username">
            {#if (!userName || userName.replace(/\s/g, "") === "") && submitted}
              <p class="text-red-500 text-xs italic">Please input a username.</p>
            {/if}
          </div>
          <div class="mb-4">
              <label class="block text-grey-darker text-sm font-bold mb-2" for="email">
                Email Address
              </label>
              <input bind:value={email} class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker mb-3" id="email" type="text" name="email" placeholder="abcd12@durham.ac.uk">
              {#if (!email || email.replace(/\s/g, "") === "") && submitted}
                <p class="text-red-500 text-xs italic">Please input a username.</p>
              {/if}
            </div>
          <div class="mb-6">
            <label class="block text-grey-darker text-sm font-bold mb-2" for="password">
              Password
            </label>
            <input bind:value={pass} class="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" id="password" name="password" type="password" placeholder="******************">
            {#if (!pass || pass.replace(/\s/g, "") === "") && submitted}
              <!--Can add checks for security of a password here-->
              <p class="text-red-500 text-xs italic">Please input a password.</p>
            {/if}
          </div>
          <div class="mb-6">
              <label class="block text-grey-darker text-sm font-bold mb-2" for="passwordAgain">
                Re-enter password
              </label>
              <input bind:value={passAgain} class="shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3" id="passwordAgain" name="passAgain" type="password" placeholder="******************">
              {#if pass && (passAgain !== pass || !passAgain)}
                <p class="text-red-500 text-xs italic">Your passwords do not match</p>
              {/if}
            </div>
          <div class="flex items-center justify-center ">
            <button type="submit" class="inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker">
              Register your account
            </button>
          </div>
        </form>
    </div>
</div>