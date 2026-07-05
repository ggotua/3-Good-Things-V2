<script>
  export let page = "home";
  export let user = null;
  export let onLogout = () => {};

  function navigate(page) {
    window.location.hash = page;
  }
</script>

<nav class="bg-white shadow">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex">
        <div
          class="flex-shrink-0 flex items-center cursor-pointer"
          on:click={() => navigate("home")}
        >
          <h1 class="text-xl font-bold text-blue-600">Daily Reflections</h1>
        </div>
      </div>
      <div class="flex items-center">
        {#if user}
          <button
            class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50"
            on:click={() => navigate("dashboard")}>Dashboard</button
          >
          <button
            class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
            on:click={() => navigate("reflect")}>New Reflection</button
          >
          <button
            class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-red-600 hover:text-red-800"
            on:click={onLogout}>Logout</button
          >
        {:else}
          <button
            class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900"
            on:click={() => navigate("login")}>Login</button
          >
          <button
            class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-white bg-blue-600 hover:bg-blue-700"
            on:click={() => navigate("register")}>Register</button
          >
        {/if}
      </div>
    </div>
  </div>
</nav>
