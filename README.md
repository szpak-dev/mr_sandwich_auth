# Authentication
This is our first Bounded Context. For microservices, there maybe a little too many responsibilities, but we have 
decided to make a split of our Monolith to Microservices using Bounded Contexts, so here we are. Authentication is not
strictly a business rule, but it fits into a Domain as a feature list required for recognizing users.

## Hosts
| Hostname | Development    | Compose/Swarm     |
|---------|----------------|-------------------|
|**auth**     | 127.0.0.1:8000 | mr.localhost/auth/* |
|**auth_worker**| manually       | -                 |
|**auth_db**| localhost:5433 | auth_db:5432      |

## Architecture
Architecture used for the software is called 
[Ports and Adapters](https://herbertograca.com/2017/09/14/ports-adapters-architecture/). In this philosophy of code 
organization, we separate business logic from the source of the data. It doesn't matter where the data comes form, it 
may be a database, an HTTP endpoint or even a file. The same goes with an input, it can be an HTTP request, CLI command
or a worker process executing a specific tasks.

### Ports
**Ports** define how **Domain** expects to be driven (input) and how it drives (data infrastructure). Every port 
declared as an **Interface** must have a corresponding **Adapter**.

### Adapters
Adapters are the implementations of the their **Adapters**. What is important here, is that we use an Inversion of 
Control (IoC), so Adapters are loaded by their abstraction (interface) instead of concrete implementation. It abstracts 
out how data is provided, and focuses on the data itself. It works on both, driving and driven ports.

### More on Ports And Adapters
There is a whole article on the blog concerning this architecture, which can be found here: 
[Ports And Adapters on Information Technology by Tomasz Szpak](https://www.szpak.dev/blog/architecture/software/ports-and-adapters).

## Files And Directories
If you take a closer look on the files and directories, this is what you will see.

### main.py
Entrypoint for the REST API, usually handled by the framework. Inside every function there is a specific use case,
which will be executed using input data from HTTP request.

### use_cases
This is the first directory you should look into. It contains modules, which names describe what a given use case does.
In our case every use case is driven by HTTP request, so for the sake of simplicity we put there some HTTP-specific 
calls, but when there are different ports, use cases must be data-agnostic.

### domain
This is the directory where our Domain-Driven Design building blocks live.

* ports
  * directory containing all the **Ports** required by the given **Aggregate**
  * they come in a form of interfaces or abstract classes

* _entities.py_
  * module holding **Entities**
  * some of them may be an Aggregate Root

* _value_objects.py_
  * holds all the Value Objects

* _errors.py_
  * contains all exceptions which can be raised when running the business logic
  * does not include adapter-specific errors

* _events.py_
  * list of all **Domain Events** emitted by **Aggregate Roots**

* _services.py_
  * **Domain Services** that orchestrates **Entities** and **Value Objects**
  * for complex cases
  * data source-agnostic, so they are not dependent on **Repositories**.

### adapters
Place for the concrete implementations of the **Ports**. The **Driven** ones lays directly in the **adapters** directory,
the **Driving** ones are in the **driving** folder.

### shared
Directory for the classes and functions which might be called from anywhere in the code. You may also put them into 
some distributed module, when the same procedures are present in other Microservices.

### _migrations
Contains database migrations. The directory is prefixed with an underscore, which is a Pythonic convention for private
parts and to point out that this is not a part of the code architecture.

## Summary
In this Microservice, I have used **Ports And Adapters** architecture. It gave us a holy grail of a good software 
project: **loose coupling** and **high cohesion**. This is a battle-tested and production-ready setup, so you can use 
it in your professional project.
