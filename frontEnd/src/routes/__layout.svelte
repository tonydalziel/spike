<script>
    import Nav from '../components/navbar.svelte';
</script>

<Nav></Nav>
<slot></slot>
<!--May want to include a wrapper around the slot if multiple pages want to be centered-->
<style>
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
</style>