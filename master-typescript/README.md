- Install `ts-node` and `typescript`: `npm install -g ts-node typescript`
- Run the TypeScript file: `ts-node path/to/your/file.ts`
- Note: If you're working on a larger project, it's a good practice to install the `ts-node` and `typescript` as dev dependencies in your project.
    - `npm install --save-dev ts-node typescript`

- Initialize the new Node.js project
    - Create a new `package.json`: `npm init -y`
    - Install the TypeScript: `npm install --save-dev typescript`
    - Initialize a TypeScript configuration file: Run the following command to create a new `tsconfig.json` file --> `tsc --init`
    - Create your source directory: `mkdir src`
    - Compile your TS code: `tsc`
    - Run your compiled code: `node dist/index.js`
    - (Optinal) Add script --> add script to your `package.json`
    ```json
        "scripts": {
          "build": "tsc",
          "start": "node dist/index.js"
        }
    ```
        - Now you can run `npm run build` to compile your TypeScript code and `npm run start` to run the compiled code.