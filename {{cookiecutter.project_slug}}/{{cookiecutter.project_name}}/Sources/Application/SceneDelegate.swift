//
//  SceneDelegate.swift
//  {{ cookiecutter.project_name }}
//
//  Created by {{ cookiecutter.author_name }}.
//

import UIKit
import SwiftUI

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        print("🎬 SceneDelegate: willConnectToSession")
        guard let windowScene = (scene as? UIWindowScene) else {
            print("❌ SceneDelegate: scene is not UIWindowScene")
            return
        }

        // Setup window
        let window = UIWindow(windowScene: windowScene)
        window.backgroundColor = .systemBackground
        self.window = window

        // Set initial screen
        showInitialScreen()
    }

    private func showInitialScreen() {
        print("🔄 SceneDelegate: Showing MainScreen")

        let mainScreenView = MainScreenModuleImpl.build()

        setRootView(mainScreenView)
    }

    private func setRootView<V: View>(_ view: V) {
        guard let window else {
            print("❌ SceneDelegate: window not found")
            return
        }

        let hostingController = UIHostingController(rootView: view)
        hostingController.view.backgroundColor = .systemBackground
        window.rootViewController = hostingController
        window.makeKeyAndVisible()
    }

    func sceneDidDisconnect(_ scene: UIScene) {
        // Called as the scene is being released by the system.
    }

    func sceneDidBecomeActive(_ scene: UIScene) {
        // Called when the scene has moved from an inactive state to an active state.
    }

    func sceneWillResignActive(_ scene: UIScene) {
        // Called when the scene will move from an active state to an inactive state.
    }

    func sceneWillEnterForeground(_ scene: UIScene) {
        // Called as the scene transitions from the background to the foreground.
    }

    func sceneDidEnterBackground(_ scene: UIScene) {
        // Called as the scene transitions from the foreground to the background.
    }
}


