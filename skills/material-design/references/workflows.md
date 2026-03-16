# Material Design workflows

## Establish the target

- confirm product context and target platform
- confirm component library choice such as Angular Material, MUI, or Material Web
- confirm token and theme system
- confirm brand latitude and accessibility requirements

## Day-two workflow

- start from tokens and hierarchy before polishing visual details
- map generic guidance into the chosen library carefully
- review navigation, state feedback, and accessibility together
- use screenshots or previews for shared theme changes

## Concrete scenario patterns

### Review a busy dashboard before a token cleanup

- compare one real dashboard screen in light and dark themes
- check whether emphasis, density, and spacing still communicate primary actions clearly
- trace each override back to the shared theme layer before proposing new component-level CSS

### Map Material 3 tokens into an existing library

- identify where color, type, shape, and motion tokens actually live in MUI, Angular Material, or Material Web
- change one token family at a time and verify the result in Storybook or a real screen
- document any intentional divergence from stock Material guidance so the next change does not reintroduce drift

## Common commands

```bash
# Example host-framework loops for Material-based systems
npm run dev
npm run storybook
```

```bash
npm run test
npm run lint
```

## Verification

- review and inspect one real screen or Storybook state before and after the change, then confirm hierarchy, spacing, density, and emphasis still read clearly
- run an accessibility pass such as keyboard navigation, contrast checks, and reduced-motion review on the affected interaction
- verify that tokens changed in the design-system layer rather than as scattered per-component overrides
- confirm screenshots or snapshot baselines changed only where the shared theme decision intended them to change

## Troubleshooting and recovery

- if a customized component loses semantic behavior, roll back to the stock library primitive first and re-apply styling through tokens or sanctioned slots
- if theme drift appears, centralize the token change in the theme layer and remove duplicated feature-level overrides
- if density, motion, or navigation updates feel noisy, compare screenshots and interaction recordings and revert to the smallest stable token set
- if a Material library wrapper fights the design intent, capture the mismatch as an explicit divergence note instead of layering more one-off overrides
