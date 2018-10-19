/* When activtity configuration is changed (eg. screen orientation) it's not allowed to commit transactions with FragmentManager,
but there it is allowed to commit transactions via FragmentManager provided by Fragment.fragmentManager */

// Activity
// 1. Change configuration
// 2. Try to replace fragment
// 3. FragmentManager throws IllegalStateException

// Fragment
// 1. Change configuration
// 2. Try to replace fragment
// 3. Fragment is replaced
