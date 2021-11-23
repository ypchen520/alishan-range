# Async Callback Functions

* [Keep Your Promises in TypeScript using async/await 2018] https://blog.bitsrc.io/keep-your-promises-in-typescript-using-async-await-7bdc57041308
* Write a Promise and use it in async await
  * help simplify the code inside functions like setTimeout

## Async/Await

### Await

* a piece of code should asynchronously wait on some other piece of code
* **task-based asynchronous methods**

### Asynchronous Functions with async await

* Using async await lets us use Promises in a reliable and safe way. 
  * This method prevents chances of any programming errors
* **An async function always returns a Promise**
  * The Promise resolves to value that is returned by the function

## Promise

```TypeScript
const one = new Promise<string>((resolve, reject) => {});
```

* take in string as the generic type for the Promise’s **resolve** value 
* The promise constructor takes an **executor** callback which the compiler will call by the runtime with these two arguments:
  * resolve: a function that is used to resolve the promise: ```.then()```
  * reject: a function that is used to reject the promise: ```.catch()```

```TypeScript
one.then(value => {
  console.log('resolved', value);
});
one.catch(error => {
  console.log('rejected', error);
});
```