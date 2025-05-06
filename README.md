# reflex-upload-bug

Demonstration of a bug where rendering an `rx.upload()` inside an `rx.foreach()` results in a JavaScript error.

Usage:

```shell
uv run -- reflex run
```

Visit http://localhost:3000 and observe:

```
Error: ./pages/index.js
  [31mx[0m Unexpected token `=`. Expected jsx identifier
    ,-[[36;1;4m/Users/spencer/Dev/elliottsj/reflex-upload-bug/.web/pages/index.js[0m:36:1]
 [2m33[0m |     <Fragment>
 [2m34[0m | 
 [2m35[0m | <>{ ["field1"].map((field, index_a684754544537562) => (
 [2m36[0m |   < key={index_a684754544537562}>
    : [35;1m       ^[0m
 [2m37[0m | 
 [2m38[0m | <RadixThemesBox className={"rx-Upload"} css={({ ["border"] : "1px dashed var(--accent-12)", ["padding"] : "5em", ["textAlign"] : "center" })} id={"upload"} ref={ref_upload} {...vnyntwet()}>
    `----

Caused by:
    Syntax Error

Import trace for requested module:
./pages/index.js
    at BuildError (webpack-internal:///(pages-dir-browser)/./node_modules/next/dist/client/components/react-dev-overlay/ui/container/build-error.js:43:41)
    at react-stack-bottom-frame (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:23864:20)
    at renderWithHooks (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:5530:22)
    at updateFunctionComponent (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:8898:19)
    at beginWork (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:10523:18)
    at runWithFiberInDEV (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:1520:30)
    at performUnitOfWork (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:15133:22)
    at workLoopSync (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:14957:41)
    at renderRootSync (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:14937:11)
    at performWorkOnRoot (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:14420:13)
    at performWorkOnRootViaSchedulerTask (webpack-internal:///(pages-dir-browser)/./node_modules/react-dom/cjs/react-dom-client.development.js:16217:7)
    at MessagePort.performWorkUntilDeadline (webpack-internal:///(pages-dir-browser)/./node_modules/scheduler/cjs/scheduler.development.js:45:48)
```
