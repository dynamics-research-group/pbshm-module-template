<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>

<body>
<h1>Creating Modules within the PBSHM Ecosystem</h1>
<h2>Overview</h2>
<p>The PBSHM Ecosystem works under the premise of a <a href="https://github.com/dynamics-research-group/pbshm-flask-core">core technical library (known as PBSHM core)</a> with additional functionality provided through modules which are included into the core. Several popular modules and the core library are also packaged together in as a singular package through the <a href="https://github.com/dynamics-research-group/pbshm-framework">PBSHM framework</a>.<p>

<p>To integrate a PBSHM module with the core, certain files are required to be created and modified; whilst this can be done manually, it is also possible to template these operation to ease development of modules. This repository uses <a href="https://cookiecutter.readthedocs.io/en/stable/">Cookiecutter</a> to provide this aforementioned template functionality to provide a blank project for module development.</p>

<h2>Creating a New Module</h2>

<p>When using <a href="https://cookiecutter.readthedocs.io/en/stable/">Cookiecutter</a> and the template project included within this repository, the user is prompted with a few questions to customise the blank project generation dependent upon the module creator's requirements.</p>

<p>For people who are familiar with PBSHM core/framework and cookiecutter, there is a short explanation <a href="#short-installation-instructions">here</a>. For those who would like a more detailed walkthrough, detailed instructions are included <a href="#detailed-installation-instructions">here</a>.

<h3>Short Installation Instructions</h3>
<ol>
  <li>Create a new virtual environment with Python 3.9.18+ and activate the virtual environment.</li>
  <li>Install cookiecutter via <code>pip</code>
    <pre><code>pip install cookiecutter</code></pre>
  </li>
  <li>
  </li>Generate blank project using <code>cookiecutter</code>
    <pre><code>cookiecutter gh:dynamics-research-group/pbshm-module-template</code></pre>
    This will prompt you to answer several questions which will customise your blank project to your requirements.
  </li>
  <li>Setup the core library as <a href="https://github.com/dynamics-research-group/pbshm-flask-core?tab=readme-ov-file#setup">described in the documentation</a>.</li>
</ol>

<h3>Detailed Installation Instructions</h3>

<ol>
  <li>
    <strong>Check Python Version</strong>
    <p>When running the cookiecutter command, you will be prompted to install either <a href="https://github.com/dynamics-research-group/pbshm-framework">Framework</a> or <a href="https://github.com/dynamics-research-group/pbshm-flask-core">Core</a>. Therefore, before running this command, you must ensure that your Python version satisfies the requirements of your choice. The Python version requirement can be found within the <code>pyproject.toml</code> file inside their respective GitHub repositories. You can find your Python version by running the command in your terminal</p>
    <pre><code>python --version</code></pre>
  </li>

  <li>
    <strong>Install Cookiecutter</strong>
    <p>To create a new PBSHM module inside the parent software, you first need to install <a href="https://cookiecutter.readthedocs.io/en/stable/">Cookiecutter</a>. Cookiecutter is a command-line utility that creates projects from templates, facilitating easy module scaffolding. Follow the installation instructions for Cookiecutter to get started. You can find the full documentation and installation guidelines at the <a href="https://cookiecutter.readthedocs.io/en/latest/installation.html">Cookiecutter official website</a>.</p>
    <p>Given a working Python installation, the following command should suffice:</p>
    <pre><code>pip install cookiecutter</code></pre>
  </li>

  <li>
    <strong>Generate Module Structure</strong>
    <p>Once Cookiecutter is installed, generate your new module structure by running the following command inside the terminal of an empty directory:</p>
    <pre><code>cookiecutter gh:dynamics-research-group/pbshm-module-template</code></pre>
    <p>Running this Cookiecutter command will prompt you to enter details about the module you intend to create, ensuring a customised and ready-to-use module structure tailored to your needs. Note that this process may take around a minute, as a new virtual environment is created under the name <code>env</code>, and the parent software is installed inside <code>env</code>.</p>
  </li>

  <li>
    <strong>Define Environment Variables</strong>
    <p>After the module has been created, you need to activate the virtual environment <code>env</code> and define the environment variable<sup><a href="footnote1">1</a></sup> <code>FLASK_APP</code> with the namespace you entered in the Cookiecutter prompt (the default is <code>mynamespace</code>). Additionally, during the module development process, it is beneficial to define the environment variable <code>FLASK_DEBUG=1</code> to ensure module changes are loaded upon refreshing the module in your browser.</p>
    <p><sup id="footnote1">1</sup> The command to define environment variables depends on your OS. Unix-based uses <code>export</code> and the Windows command prompt uses <code>set</code>.</p>
  </li>

  <li>
    <strong>Configuring the Module</strong>
    <p>Module configuration is the same regardless of the choice for PBSHM Flask Core or PBSHM Framework. This process serves to connect your module to your MongoDB process. To configure MongoDB to your module, run the command
    <pre><code>flask init config</code></pre></p>
    <p>Running this command will give the following prompts:</p>
    <ol type="a">
      <li><em>Hostname [localhost]:</em> This is the host connection, for development and debugging processes, this is likely to localhost.</li>
      <li><em>Port [27017]:</em> This is the port where the database is found. MongoDB's default port is 27017.</li>
      <li><em>Authentication database [admin]:</em> Inside the connection the prescribed port, is the name of the database that contains the admin account.</li>
      <li><em>Database username:</em> This is the username, with root access to the database.</li>
      <li><em>Database password:</em> This is the password for the previous prompt.</li>
      <li><em>Repeat for confirmation:</em> Repetition to ensure the correct password.</li>
      <li><em>PBSHM database [drg-pbshm]:</em> This is the name of the database that stores the data for use within the module.</li>
      <li><em>Users collection [users]:</em> This is the collection inside the previously given database, which contains the user credentials.</li>
      <li><em>Default data collection [structures]:</em> The collection which contains the PBSHM data.</li>
      <li><em>Secret Key []:</em></li>
    </ol>
    <p>These commands all serve to point the module you are creating in the direction of the data that you have collected/ wish to manipulate via the module you create.</p>
    <p>Running the second flask command <pre><code>flask init db new-root-user</code></pre> creates the login details into the Framework/ Core. Note, if you have already ran this command inside the database there will already be accounts within. These login credentials are stored within the database and are only required to be ran once per database.</p>
    <p>Upon running this command you are prompted with:</p>
    <ol>
      <li>Email address</li>
      <li>Password</li>
      <li>Repeat for confirmation</li>
      <li>Your first name</li>
      <li>Your second name</li>
    </ol>
    <p>These are a lot more self-explanatory but need to be remembered to access the framework.</p>
  </li>

  <li>
    <strong>Running the Module</strong>
    <p>After successfully configuring the database and creating an account, the module is all set and activated by running <pre><code>flask run</code></pre></p>
  </li>
</ol>
</body>
</html>
