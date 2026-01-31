<script>
  import { onMount } from "svelte";
  import Navbar from "./Navbar.svelte";
  import "./app.css";

  import Login from "./Login.svelte";
  import Register from "./Register.svelte";
  import Dashboard from "./Dashboard.svelte";
  import Reflect from "./Reflect.svelte";

  let page = "home";
  let user = null; // null means not logged in

  // Basic user check (to be replaced with API)
  let loading = true;

  function handleHashChange() {
    const hash = window.location.hash.slice(1);
    page = hash || "home";
  }

  onMount(async () => {
    window.addEventListener("hashchange", handleHashChange);
    handleHashChange();

    // Check auth status
    try {
      const res = await fetch("/api/user");
      if (res.ok) {
        const data = await res.json();
        user = data.user;
        // If on login/register page and logged in, redirect to dashboard
        if (page === "login" || page === "register") {
          window.location.hash = "dashboard";
        }
      } else {
        user = null;
      }
    } catch (e) {
      console.error(e);
    }
    loading = false;
  });
</script>

<div class="min-h-screen bg-gray-50">
  <Navbar {user} {page} />

  <main class="py-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      {#if page === "home"}
        <div class="text-center">
          <h1
            class="text-4xl font-extrabold text-gray-900 sm:text-5xl sm:tracking-tight lg:text-6xl"
          >
            Track Your Daily Achievements
          </h1>
          <p class="mt-5 max-w-xl mx-auto text-xl text-gray-500">
            Take a moment each day to reflect on your accomplishments. Build
            confidence and resilience.
          </p>
          <div class="mt-8 flex justify-center">
            <button
              class="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700"
              on:click={() => (window.location.hash = "register")}
            >
              Get Started
            </button>
          </div>
        </div>
      {:else if page === "login"}
        <Login />
      {:else if page === "register"}
        <Register />
      {:else if page === "dashboard"}
        <Dashboard />
      {:else if page === "reflect"}
        <Reflect />
      {:else}
        <p class="text-center text-gray-500">Page not found: {page}</p>
      {/if}
    </div>
  </main>
</div>
