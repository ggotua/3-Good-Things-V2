<script>
    let username = "";
    let password = "";
    let error = "";

    async function handleLogin() {
        try {
            const res = await fetch("/api/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });
            const data = await res.json();

            if (res.ok) {
                window.location.reload(); // Reload to update auth state in App
            } else {
                error = data.error || "Login failed";
            }
        } catch (e) {
            error = "An error occurred";
        }
    }
</script>

<div class="max-w-md mx-auto bg-white rounded-lg shadow overflow-hidden">
    <div class="px-6 py-8">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-8">Login</h2>
        {#if error}
            <div
                class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4"
            >
                {error}
            </div>
        {/if}
        <form on:submit|preventDefault={handleLogin}>
            <div class="mb-4">
                <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="username"
                >
                    Username
                </label>
                <input
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="username"
                    type="text"
                    bind:value={username}
                />
            </div>
            <div class="mb-6">
                <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="password"
                >
                    Password
                </label>
                <input
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="password"
                    type="password"
                    bind:value={password}
                />
            </div>
            <div class="flex items-center justify-between">
                <button
                    class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full transform transition hover:scale-105 duration-300 ease-in-out"
                    type="submit"
                >
                    Sign In
                </button>
            </div>
        </form>
        <div class="mt-4 text-center">
            <p class="text-sm text-gray-600">
                Don't have an account? <a
                    href="#register"
                    class="text-blue-600 hover:underline">Register</a
                >
            </p>
        </div>
    </div>
</div>
