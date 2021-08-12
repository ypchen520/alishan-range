# Getting started

## Component

* **display** data on the screen,
* **listen** for user input, and
* **take action** based on that input
* includes
  * Component class
  * HTML template
  * Component-specific styles
* AppComponent

### Component class

* app.component.ts
* heroes.component.ts
* Always **export** the component class so you can import it elsewhere
* add property

#### @Component

* a decorator function that specifies the Angular **metadata**
* three metadata properties
  * selector: **the component's CSS element selector**
    * app-herpes
      * matches the **name of the HTML element** that identifies this component within a parent component's template
  * templateUrl
  * styleUrls

#### ngOnInit()

* a lifecycle hook
* called shortly after creating a component
* a good place to put initialization logic

#### Show the HeroesComponent view

* display
  * add it to the **template** of the shell AppComponent
    * element selector: ```<app-heroes>```

### Create a Hero interface

* Create a Hero interface in its own file in the src/app folder
* Give it properties

### HTML template

* app.component.html
* heroes.component.html

#### Pipes (|)

* UppercasePipe

```typescript
<h2>{{hero.name | uppercase}} Details</h2>
```

* format strings, currency amounts, dates and other **display data**
* Angular ships with several built-in pipes and you can **create your own**

#### Edit

* Users should be able to edit the hero name in an <input> textbox
  * The textbox should
    * **display** the hero's name property: data flows from the component class out to the screen
    * **update** the property: data flows from the screen back to the class
* **Two-way binding**
  * two-way data flow: setup a two-way data binding between the <input> form element and the hero.name property
  * [(ngModel)]
    * It belongs to the optional FormsModule and you must opt-in to using it.

```html
<div>
  <label for="name">Hero name: </label>
  <input id="name" [(ngModel)]="hero.name" placeholder="name">
</div>
```

### Component-specific styles

* app.component.css
* heroes.component.css

## AppModule

* metadata
  * files and libraries the app requires
  * some in the @Component decorators
  * **@NgModule decorator: top-level AppModule class**
    * src/app/app.module.ts
      * imports: []

### Declare HeroesComponent

* **Every component must be declared in exactly one NgModule**
  * declarations: []

## Create a new workspace and an initial application

* Ensure that you are not already in an Angular workspace folder
* ```ng new PROJECT NAME```
  * A new workspace, with a root folder named PROJECT NAME
  * An initial skeleton app project, also called PROJECT NAME (src/)
  * An end-to-end test project (in the e2e subfolder)
  * Related configuration files

## Interpolation binding

```typescript
<h1>{{title}}</h1>
```

* The double curly braces

## Global style

* a consistent look across the application
* src/styles.css: application-wide styles

## Create a component

* ```ng generate component heroes```
  * ```src/app/heroes```
    * heroes.component.ts
    * heroes.component.html
    * heroes.component.css