# 2geda Events API Documentation

<p>Welcome to the 2geda Events API! Below you'll find the list of available endpoints and their functionalities.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#endpoints">Endpoints</a></li>
    <ul>
        <li><a href="#get-endpoints">GET Endpoints</a></li>
        <li><a href="#post-endpoint">POST Endpoint</a></li>
        <li><a href="#put-endpoint">PUT Endpoint</a></li>
    </ul>
    <li><a href="#authentication">Authentication</a></li>
    <ul>
        <li><a href="#request-token">Request Token</a></li>
        <li><a href="#sign-up">Sign Up</a></li>
    </ul>
    <li><a href="#database">Database</a></li>
</ul>

<h2 id="endpoints">Endpoints</h2>

<h3 id="get-endpoints">GET Endpoints</h3>
<ul>
    <li><strong>Get All Events:</strong> <code>/api/events/</code> (No authentication required)</li>
</ul>

<h3 id="post-endpoint">POST Endpoint</h3>
<ul>
    <li><strong>Create an Event:</strong> <code>/api/events/</code></li>
</ul>

<h3 id="put-endpoint">PUT Endpoint</h3>
<ul>
    <li><strong>Update an Event:</strong> <code>/api/events/id/</code></li>
</ul>

<h2 id="authentication">Authentication</h2>
<p>To perform certain actions like creating or updating events, authentication is required.</p>
<ul>
    <li><strong>Request Token:</strong> <code>/authtoken/token/login/</code></li>
    <li><strong>Sign Up:</strong> <code>/auth/users/</code></li>
</ul>

<h2 id="database">Database</h2>
<p>The database used for this API is PostgreSQL.</p>
