// // // import { motion } from "framer-motion";

// // // export default function HomeLanding({ setActiveTab }) {
// // //   return (
// // //     <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-blue-50 to-white dark:from-gray-900 dark:to-gray-950 transition-all duration-300">
// // //       {/* Hero Section */}
// // //       <section className="text-center max-w-3xl mt-20">
// // //         <motion.h1
// // //           className="text-5xl font-extrabold text-gray-900 dark:text-white mb-4"
// // //           initial={{ opacity: 0, y: 20 }}
// // //           animate={{ opacity: 1, y: 0 }}
// // //           transition={{ duration: 0.7 }}
// // //         >
// // //           Analyze your website’s SEO performance for free!
// // //         </motion.h1>
// // //         <p className="text-gray-600 dark:text-gray-400 text-lg mb-8">
// // //           Get a complete SEO report and discover how to improve your website’s visibility.
// // //         </p>

// // //         <div className="flex flex-col sm:flex-row justify-center gap-3">
// // //           <input
// // //             type="text"
// // //             placeholder="Enter your website URL (e.g. example.com)"
// // //             className="px-5 py-3 w-80 sm:w-96 rounded-xl border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:outline-none"
// // //           />
// // //           <button
// // //             onClick={() => setActiveTab("analyzer")}
// // //             className="px-6 py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition"
// // //           >
// // //             Checkup Now 🚀
// // //           </button>
// // //         </div>
// // //       </section>

// // //       {/* Features Section */}
// // //       <section className="mt-24 grid grid-cols-1 md:grid-cols-3 gap-8 px-6 max-w-6xl">
// // //         {[
// // //           {
// // //             icon: "🔍",
// // //             title: "On-Page SEO Analysis",
// // //             desc: "Check meta tags, titles, and content optimization for your site.",
// // //           },
// // //           {
// // //             icon: "⚡",
// // //             title: "Performance Insights",
// // //             desc: "Analyze your site’s loading speed, Core Web Vitals, and user experience.",
// // //           },
// // //           {
// // //             icon: "🔗",
// // //             title: "Backlink Overview",
// // //             desc: "Understand your backlink profile and opportunities to improve rankings.",
// // //           },
// // //         ].map((item, index) => (
// // //           <motion.div
// // //             key={index}
// // //             whileHover={{ scale: 1.05 }}
// // //             className="bg-white dark:bg-gray-800 rounded-2xl shadow-md p-6 text-center"
// // //           >
// // //             <div className="text-4xl mb-3">{item.icon}</div>
// // //             <h3 className="font-bold text-lg mb-2 text-gray-900 dark:text-white">
// // //               {item.title}
// // //             </h3>
// // //             <p className="text-gray-600 dark:text-gray-400 text-sm">
// // //               {item.desc}
// // //             </p>
// // //           </motion.div>
// // //         ))}
// // //       </section>

// // //       {/* CTA */}
// // //       <section className="mt-20 mb-16 text-center">
// // //         <motion.h2
// // //           className="text-3xl font-semibold text-gray-900 dark:text-white mb-4"
// // //           initial={{ opacity: 0 }}
// // //           whileInView={{ opacity: 1 }}
// // //         >
// // //           Improve your website SEO today
// // //         </motion.h2>
// // //         <button
// // //           onClick={() => setActiveTab("dashboard")}
// // //           className="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-full hover:opacity-90 transition"
// // //         >
// // //           Go to Dashboard →
// // //         </button>
// // //       </section>
// // //     </div>
// // //   );
// // // }



// // import { motion } from "framer-motion";
// // import Galaxy from "./Galaxy";

// // export default function HomeLanding({ setActiveTab }) {
// //   return (
// //     <div className="relative bg-white dark:bg-gray-950">
// //       {/* Hero Section with Galaxy Background */}
// //       <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-950">
// //         {/* Galaxy Background */}
// //         <div className="absolute inset-0 opacity-30 dark:opacity-50">
// //           <Galaxy
// //             mouseRepulsion={true}
// //             mouseInteraction={true}
// //             density={1.2}
// //             glowIntensity={0.4}
// //             saturation={0.3}
// //             hueShift={200}
// //             rotationSpeed={0.05}
// //           />
// //         </div>

// //         <div className="relative z-10 text-center max-w-5xl px-6 py-20">
// //           <motion.h1
// //             className="text-5xl md:text-6xl lg:text-7xl font-bold text-gray-900 dark:text-white mb-8 leading-tight"
// //             initial={{ opacity: 0, y: 30 }}
// //             animate={{ opacity: 1, y: 0 }}
// //             transition={{ duration: 0.8 }}
// //           >
// //             "SEO Site Checkup runs through a fast audit of your site, checking for proper tags and surfacing any errors that might come up."
// //           </motion.h1>

// //           {/* Company Logos */}
// //           <motion.div
// //             className="flex flex-wrap items-center justify-center gap-12 mt-12 mb-16"
// //             initial={{ opacity: 0 }}
// //             animate={{ opacity: 1 }}
// //             transition={{ delay: 0.3, duration: 0.8 }}
// //           >
// //             <div className="text-3xl font-bold text-gray-800 dark:text-gray-200">Buffer</div>
// //             <div className="text-3xl font-bold text-gray-400 dark:text-gray-500">HUFFPOST</div>
// //             <div className="text-3xl font-bold text-gray-300 dark:text-gray-600">groove</div>
// //           </motion.div>

// //           {/* CTA Scroll Indicator */}
// //           <motion.div
// //             className="mt-16"
// //             initial={{ opacity: 0 }}
// //             animate={{ opacity: 1 }}
// //             transition={{ delay: 0.6, duration: 0.8 }}
// //           >
// //             <div className="inline-block text-sm text-gray-500 dark:text-gray-400">
// //               Scroll to explore
// //             </div>
// //           </motion.div>
// //         </div>
// //       </section>

// //       {/* Benefits Section with Illustration */}
// //       <section className="py-20 px-6 bg-white dark:bg-gray-950">
// //         <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
// //           {/* Illustration */}
// //           <motion.div
// //             className="relative"
// //             initial={{ opacity: 0, x: -50 }}
// //             whileInView={{ opacity: 1, x: 0 }}
// //             transition={{ duration: 0.6 }}
// //             viewport={{ once: true }}
// //           >
// //             <div className="relative w-full aspect-square">
// //               <div className="absolute inset-0 bg-gradient-to-br from-orange-400 to-orange-600 rounded-full opacity-90"></div>
// //               <div className="absolute inset-0 flex items-center justify-center">
// //                 <div className="text-white text-6xl">🚀</div>
// //               </div>
// //             </div>
// //           </motion.div>

// //           {/* Benefits Text */}
// //           <motion.div
// //             initial={{ opacity: 0, x: 50 }}
// //             whileInView={{ opacity: 1, x: 0 }}
// //             transition={{ duration: 0.6 }}
// //             viewport={{ once: true }}
// //           >
// //             <h2 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-6">
// //               Everything you need to uplift your business
// //             </h2>
            
// //             <div className="space-y-6">
// //               <div>
// //                 <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">
// //                   SEO doesn't need to be difficult
// //                 </h3>
// //                 <p className="text-gray-600 dark:text-gray-400">
// //                   We provide a set of SEO tools to help you understand your website from a search engine's perspective.
// //                 </p>
// //               </div>

// //               <div>
// //                 <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">
// //                   Know when to act and improve
// //                 </h3>
// //                 <p className="text-gray-600 dark:text-gray-400">
// //                   Our SEO reports also let you know of any problems or technical shortcomings in your website that may be hurting your search engine rankings.
// //                 </p>
// //               </div>

// //               <div>
// //                 <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">
// //                   Dedicated team of SEO professionals
// //                 </h3>
// //                 <p className="text-gray-600 dark:text-gray-400">
// //                   We've seen how algorithms, penalties and SEO factors have evolved since the early days of search. As SEO professionals and site owners, we know first-hand where webmasters need to focus and spend their time.
// //                 </p>
// //               </div>

// //               <button
// //                 onClick={() => setActiveTab("analyzer")}
// //                 className="mt-6 px-8 py-4 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
// //               >
// //                 I'm Ready For A 7-Day Free Trial
// //               </button>
// //             </div>
// //           </motion.div>
// //         </div>
// //       </section>

// //       {/* Stats Section */}
// //       <section className="py-20 px-6 bg-gradient-to-r from-blue-900 to-blue-950 text-white">
// //         <div className="max-w-7xl mx-auto">
// //           <motion.h2
// //             className="text-3xl md:text-4xl font-bold text-center mb-16"
// //             initial={{ opacity: 0, y: 20 }}
// //             whileInView={{ opacity: 1, y: 0 }}
// //             transition={{ duration: 0.6 }}
// //             viewport={{ once: true }}
// //           >
// //             Conveying trust by numbers is our way to do business. Is it yours too?
// //           </motion.h2>

// //           <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
// //             <motion.div
// //               className="text-center"
// //               initial={{ opacity: 0, y: 20 }}
// //               whileInView={{ opacity: 1, y: 0 }}
// //               transition={{ duration: 0.6, delay: 0.1 }}
// //               viewport={{ once: true }}
// //             >
// //               <div className="text-5xl md:text-6xl font-bold mb-4">25.5M+</div>
// //               <div className="text-lg">Unique URLs checked<br />in over 11 years</div>
// //             </motion.div>

// //             <motion.div
// //               className="text-center"
// //               initial={{ opacity: 0, y: 20 }}
// //               whileInView={{ opacity: 1, y: 0 }}
// //               transition={{ duration: 0.6, delay: 0.2 }}
// //               viewport={{ once: true }}
// //             >
// //               <div className="text-5xl md:text-6xl font-bold mb-4">85,000+</div>
// //               <div className="text-lg">Happy customers<br />all over the world</div>
// //             </motion.div>

// //             <motion.div
// //               className="text-center"
// //               initial={{ opacity: 0, y: 20 }}
// //               whileInView={{ opacity: 1, y: 0 }}
// //               transition={{ duration: 0.6, delay: 0.3 }}
// //               viewport={{ once: true }}
// //             >
// //               <div className="text-5xl md:text-6xl font-bold mb-4">120+</div>
// //               <div className="text-lg">Countries served with<br />better SEO Services</div>
// //             </motion.div>
// //           </div>
// //         </div>
// //       </section>

// //       {/* Testimonials Section */}
// //       <section className="py-20 px-6 bg-gray-50 dark:bg-gray-900">
// //         <div className="max-w-7xl mx-auto">
// //           <h2 className="text-4xl font-bold text-center text-gray-900 dark:text-white mb-16">
// //             They use us to create great experiences
// //           </h2>

// //           <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
// //             {[
// //               {
// //                 name: "Surrey",
// //                 text: "I would like to start by saying I love your website and use it as a tool to better my work.",
// //                 avatar: "👨‍💼"
// //               },
// //               {
// //                 name: "Marco",
// //                 text: "Thanks for your wonderful tool.",
// //                 avatar: "👨‍💻"
// //               },
// //               {
// //                 name: "Guy S.",
// //                 text: "Excellent service and great support team!",
// //                 avatar: "👨‍🎨"
// //               }
// //             ].map((testimonial, index) => (
// //               <motion.div
// //                 key={index}
// //                 className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-lg"
// //                 initial={{ opacity: 0, y: 20 }}
// //                 whileInView={{ opacity: 1, y: 0 }}
// //                 transition={{ duration: 0.6, delay: index * 0.1 }}
// //                 viewport={{ once: true }}
// //               >
// //                 <div className="flex items-center gap-3 mb-4">
// //                   <div className="w-12 h-12 rounded-full bg-gradient-to-br from-green-400 to-blue-500 flex items-center justify-center text-2xl">
// //                     {testimonial.avatar}
// //                   </div>
// //                   <div className="font-bold text-gray-900 dark:text-white">{testimonial.name}</div>
// //                 </div>
// //                 <p className="text-gray-600 dark:text-gray-300">{testimonial.text}</p>
// //               </motion.div>
// //             ))}
// //           </div>
// //         </div>
// //       </section>

// //       {/* Dashboard Preview Section */}
// //       <section className="py-20 px-6 bg-white dark:bg-gray-950">
// //         <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
// //           <motion.div
// //             initial={{ opacity: 0, x: -50 }}
// //             whileInView={{ opacity: 1, x: 0 }}
// //             transition={{ duration: 0.6 }}
// //             viewport={{ once: true }}
// //           >
// //             <p className="text-orange-600 font-semibold mb-2">Enjoy your Dashboard</p>
// //             <h2 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-6">
// //               Everything you need in one place
// //             </h2>
// //             <p className="text-gray-600 dark:text-gray-400 mb-6">
// //               All of the tools right at your fingertips. With one quick click, you can see how your site is doing. The dashboard offers instant access to reports, monitors, and analysis tools.
// //             </p>
// //             <button
// //               onClick={() => setActiveTab("dashboard")}
// //               className="px-8 py-3 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
// //             >
// //               Start Free Trial
// //             </button>
// //           </motion.div>

// //           <motion.div
// //             className="relative"
// //             initial={{ opacity: 0, x: 50 }}
// //             whileInView={{ opacity: 1, x: 0 }}
// //             transition={{ duration: 0.6 }}
// //             viewport={{ once: true }}
// //           >
// //             <div className="bg-gray-900 rounded-lg shadow-2xl p-4 transform hover:scale-105 transition-transform duration-300">
// //               <div className="bg-gradient-to-br from-orange-500 to-red-600 h-64 rounded flex items-center justify-center text-white text-6xl">
// //                 📊
// //               </div>
// //             </div>
// //           </motion.div>
// //         </div>
// //       </section>

// //       {/* Features Grid Section */}
// //       <section className="py-20 px-6 bg-orange-50 dark:bg-gray-900">
// //         <div className="max-w-7xl mx-auto">
// //           <p className="text-center text-orange-600 font-semibold mb-2">Tons of great features</p>
// //           <h2 className="text-4xl font-bold text-center text-gray-900 dark:text-white mb-16">
// //             Introducing our SEO ToolBox
// //           </h2>

// //           <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
// //             {[
// //               {
// //                 icon: "📈",
// //                 title: "Instantly analyze your SEO issues",
// //                 desc: "Run unlimited analysis on our most powerful servers. Stored reports make it easy to view progress and past work."
// //               },
// //               {
// //                 icon: "🔄",
// //                 title: "Professional SEO monitoring tools",
// //                 desc: "Automatically keep track of weekly changes in more than 70 SEO variables. Get notifications if your SEO score changes."
// //               },
// //               {
// //                 icon: "👥",
// //                 title: "Understand your competitors' SEO profile",
// //                 desc: "Side-by-side SEO comparisons of up to 5 competitors. See how your SEO can improve against the competition."
// //               },
// //               {
// //                 icon: "📝",
// //                 title: "Save hours with white-label SEO reports",
// //                 desc: "Quickly create editable SEO reports for your clients or partner websites."
// //               },
// //               {
// //                 icon: "💡",
// //                 title: "SEO reports you can understand and act upon",
// //                 desc: "SEO broken down in plain language, with clear definitions and 'how-to-fix' tutorials for each issue."
// //               },
// //               {
// //                 icon: "🎁",
// //                 title: "7-Day free trial, cancel anytime!",
// //                 desc: "Get started right away by registering below. Plans start at $34.95 per month."
// //               }
// //             ].map((feature, index) => (
// //               <motion.div
// //                 key={index}
// //                 className="bg-white dark:bg-gray-800 rounded-2xl p-8 text-center hover:shadow-xl transition-shadow duration-300"
// //                 initial={{ opacity: 0, y: 20 }}
// //                 whileInView={{ opacity: 1, y: 0 }}
// //                 transition={{ duration: 0.6, delay: index * 0.1 }}
// //                 viewport={{ once: true }}
// //               >
// //                 <div className="w-16 h-16 mx-auto mb-4 bg-orange-600 rounded-full flex items-center justify-center text-3xl">
// //                   {feature.icon}
// //                 </div>
// //                 <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-3">
// //                   {feature.title}
// //                 </h3>
// //                 <p className="text-gray-600 dark:text-gray-400 text-sm">
// //                   {feature.desc}
// //                 </p>
// //               </motion.div>
// //             ))}
// //           </div>
// //         </div>
// //       </section>

// //       {/* Final CTA Section */}
// //       <section className="py-20 px-6 bg-gradient-to-r from-blue-900 to-blue-950 text-white">
// //         <div className="max-w-4xl mx-auto text-center">
// //           <h2 className="text-4xl md:text-5xl font-bold mb-8">
// //             Check your website's SEO for free right now!
// //           </h2>
// //           <div className="flex flex-col sm:flex-row gap-4 justify-center max-w-3xl mx-auto">
// //             <input
// //               type="text"
// //               placeholder="Website URL"
// //               className="px-6 py-4 flex-1 rounded-lg text-gray-900 focus:outline-none focus:ring-4 focus:ring-orange-500"
// //             />
// //             <button
// //               onClick={() => setActiveTab("analyzer")}
// //               className="px-10 py-4 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
// //             >
// //               Checkup
// //             </button>
// //           </div>
// //         </div>
// //       </section>

// //       {/* Footer */}
// //       <footer className="bg-blue-950 text-white py-12 px-6">
// //         <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
// //           <div>
// //             <div className="flex items-center gap-2 mb-4">
// //               <div className="w-10 h-10 bg-orange-600 rounded flex items-center justify-center font-bold">
// //                 S
// //               </div>
// //               <span className="font-bold text-lg">SEO Site Checkup</span>
// //             </div>
// //             <p className="text-sm text-gray-300 mb-4">
// //               Website SEO, Monitoring & Automation Made Easy.
// //             </p>
// //             <div className="flex gap-3">
// //               <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center hover:bg-gray-600 cursor-pointer transition">
// //                 𝕏
// //               </div>
// //               <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center hover:bg-gray-600 cursor-pointer transition">
// //                 f
// //               </div>
// //             </div>
// //           </div>

// //           <div>
// //             <h3 className="font-bold mb-4">Product</h3>
// //             <ul className="space-y-2 text-sm text-gray-300">
// //               <li className="hover:text-white cursor-pointer">Pricing</li>
// //               <li className="hover:text-white cursor-pointer">Free Tools</li>
// //               <li className="hover:text-white cursor-pointer">Articles</li>
// //               <li className="hover:text-white cursor-pointer">Login</li>
// //               <li className="hover:text-white cursor-pointer">Free 7-Day Trial</li>
// //             </ul>
// //           </div>

// //           <div>
// //             <h3 className="font-bold mb-4">Company</h3>
// //             <ul className="space-y-2 text-sm text-gray-300">
// //               <li className="hover:text-white cursor-pointer">About us</li>
// //               <li className="hover:text-white cursor-pointer">FAQs</li>
// //               <li className="hover:text-white cursor-pointer">SEO Checkups</li>
// //               <li className="hover:text-white cursor-pointer">Contact</li>
// //             </ul>
// //           </div>

// //           <div>
// //             <h3 className="font-bold mb-4">Legal</h3>
// //             <ul className="space-y-2 text-sm text-gray-300">
// //               <li className="hover:text-white cursor-pointer">Terms of Service</li>
// //               <li className="hover:text-white cursor-pointer">Privacy Policy</li>
// //               <li className="hover:text-white cursor-pointer">Refunds Policy</li>
// //             </ul>
// //           </div>
// //         </div>

// //         <div className="max-w-7xl mx-auto mt-12 pt-8 border-t border-gray-700 text-center text-sm text-gray-400">
// //           © SEO Site Checkup 2020-2025 • All rights reserved
// //         </div>
// //       </footer>

// //       {/* Floating Scroll to Top Button */}
// //       <button
// //         onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
// //         className="fixed bottom-8 right-8 w-14 h-14 bg-orange-600 text-white rounded-full shadow-lg hover:bg-orange-700 transition flex items-center justify-center text-2xl z-50"
// //       >
// //         ↑
// //       </button>
// //     </div>
// //   );
// // }




// import { motion } from "framer-motion";
// import Galaxy from "./Galaxy";

// export default function HomeLanding({ setActiveTab }) {
//   return (
//     <div className="relative bg-gray-950 min-h-screen">
//       {/* Hero Section with Galaxy Background */}
//       <section className="relative min-h-screen flex flex-col overflow-hidden bg-gray-950">
//         {/* Galaxy Background */}
//         <div className="absolute inset-0 opacity-60">
//           <Galaxy
//             mouseRepulsion={true}
//             mouseInteraction={true}
//             density={1.2}
//             glowIntensity={0.4}
//             saturation={0.3}
//             hueShift={200}
//             rotationSpeed={0.05}
//           />
//         </div>

//         {/* Header Navigation */}
//         <motion.header
//           className="relative z-20 pt-8 px-6"
//           initial={{ opacity: 0, y: -20 }}
//           animate={{ opacity: 1, y: 0 }}
//           transition={{ duration: 0.6 }}
//         >
//           <div className="max-w-4xl mx-auto">
//             <nav className="flex items-center justify-between px-8 py-4 bg-gray-900/50 backdrop-blur-xl rounded-full border border-gray-800/50 shadow-2xl">
//               {/* Logo */}
//               <div className="flex items-center gap-3">
//                 <div className="w-8 h-8 bg-gradient-to-br from-orange-500 to-red-600 rounded-lg flex items-center justify-center">
//                   <span className="text-white font-bold text-lg">S</span>
//                 </div>
//                 <span className="text-white font-bold text-lg">SEO Checkup</span>
//               </div>

//               {/* Navigation Links */}
//               <div className="flex items-center gap-8">
//                 <button 
//                   onClick={() => setActiveTab("home")}
//                   className="text-gray-300 hover:text-white transition-colors font-medium"
//                 >
//                   Home
//                 </button>
//                 <button 
//                   onClick={() => setActiveTab("dashboard")}
//                   className="text-gray-300 hover:text-white transition-colors font-medium"
//                 >
//                   Dashboard
//                 </button>
//                 <button 
//                   onClick={() => setActiveTab("analyzer")}
//                   className="text-gray-300 hover:text-white transition-colors font-medium"
//                 >
//                   Analyzer
//                 </button>
//                 <button className="px-6 py-2 bg-white text-gray-900 font-semibold rounded-full hover:bg-gray-100 transition">
//                   Login
//                 </button>
//               </div>
//             </nav>
//           </div>
//         </motion.header>

//         {/* Hero Content */}
//         <div className="relative z-10 flex-1 flex flex-col items-center justify-center text-center px-6 py-20">
//           {/* Badge */}
//           <motion.div
//             className="inline-flex items-center gap-2 px-4 py-2 bg-gray-900/50 backdrop-blur-xl rounded-full border border-gray-800/50 mb-8"
//             initial={{ opacity: 0, scale: 0.9 }}
//             animate={{ opacity: 1, scale: 1 }}
//             transition={{ duration: 0.6, delay: 0.2 }}
//           >
//             <div className="w-5 h-5 flex items-center justify-center">
//               <div className="w-3 h-3 bg-gradient-to-br from-orange-500 to-red-600 rounded"></div>
//             </div>
//             <span className="text-gray-300 text-sm font-medium">New SEO Analysis</span>
//           </motion.div>

//           {/* Main Heading */}
//           <motion.h1
//             className="text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-8 leading-tight max-w-5xl"
//             initial={{ opacity: 0, y: 30 }}
//             animate={{ opacity: 1, y: 0 }}
//             transition={{ duration: 0.8, delay: 0.3 }}
//           >
//             Analyze your website's SEO performance for free!
//           </motion.h1>

//           <motion.p
//             className="text-xl text-gray-400 mb-12 max-w-2xl"
//             initial={{ opacity: 0, y: 20 }}
//             animate={{ opacity: 1, y: 0 }}
//             transition={{ duration: 0.8, delay: 0.4 }}
//           >
//             Get a complete SEO report and discover how to improve your website's visibility
//           </motion.p>

//           {/* CTA Buttons */}
//           <motion.div
//             className="flex flex-col sm:flex-row items-center gap-4"
//             initial={{ opacity: 0, y: 20 }}
//             animate={{ opacity: 1, y: 0 }}
//             transition={{ duration: 0.8, delay: 0.5 }}
//           >
//             <button
//               onClick={() => setActiveTab("analyzer")}
//               className="px-8 py-4 bg-white text-gray-900 font-semibold rounded-full hover:bg-gray-100 transition shadow-xl hover:shadow-2xl hover:scale-105 transform duration-300"
//             >
//               Get Started
//             </button>
//             <button className="px-8 py-4 bg-transparent text-white font-semibold rounded-full border-2 border-gray-700 hover:border-gray-500 transition hover:bg-gray-900/30">
//               Learn More
//             </button>
//           </motion.div>
//         </div>
//       </section>

//       {/* Benefits Section with Illustration */}
//       <section className="py-20 px-6 bg-gray-950">
//         <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
//           {/* Illustration */}
//           <motion.div
//             className="relative"
//             initial={{ opacity: 0, x: -50 }}
//             whileInView={{ opacity: 1, x: 0 }}
//             transition={{ duration: 0.6 }}
//             viewport={{ once: true }}
//           >
//             <div className="relative w-full aspect-square">
//               <div className="absolute inset-0 bg-gradient-to-br from-orange-400 to-orange-600 rounded-full opacity-90"></div>
//               <div className="absolute inset-0 flex items-center justify-center">
//                 <div className="text-white text-6xl">🚀</div>
//               </div>
//             </div>
//           </motion.div>

//           {/* Benefits Text */}
//           <motion.div
//             initial={{ opacity: 0, x: 50 }}
//             whileInView={{ opacity: 1, x: 0 }}
//             transition={{ duration: 0.6 }}
//             viewport={{ once: true }}
//           >
//             <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
//               Everything you need to uplift your business
//             </h2>
            
//             <div className="space-y-6">
//               <div>
//                 <h3 className="text-xl font-bold text-white mb-2">
//                   SEO doesn't need to be difficult
//                 </h3>
//                 <p className="text-gray-400">
//                   We provide a set of SEO tools to help you understand your website from a search engine's perspective.
//                 </p>
//               </div>

//               <div>
//                 <h3 className="text-xl font-bold text-white mb-2">
//                   Know when to act and improve
//                 </h3>
//                 <p className="text-gray-400">
//                   Our SEO reports also let you know of any problems or technical shortcomings in your website that may be hurting your search engine rankings.
//                 </p>
//               </div>

//               <div>
//                 <h3 className="text-xl font-bold text-white mb-2">
//                   Dedicated team of SEO professionals
//                 </h3>
//                 <p className="text-gray-400">
//                   We've seen how algorithms, penalties and SEO factors have evolved since the early days of search. As SEO professionals and site owners, we know first-hand where webmasters need to focus and spend their time.
//                 </p>
//               </div>

//               <button
//                 onClick={() => setActiveTab("analyzer")}
//                 className="mt-6 px-8 py-4 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
//               >
//                 I'm Ready For A 7-Day Free Trial
//               </button>
//             </div>
//           </motion.div>
//         </div>
//       </section>

//       {/* Stats Section */}
//       <section className="py-20 px-6 bg-gradient-to-r from-blue-900 to-blue-950 text-white">
//         <div className="max-w-7xl mx-auto">
//           <motion.h2
//             className="text-3xl md:text-4xl font-bold text-center mb-16"
//             initial={{ opacity: 0, y: 20 }}
//             whileInView={{ opacity: 1, y: 0 }}
//             transition={{ duration: 0.6 }}
//             viewport={{ once: true }}
//           >
//             Conveying trust by numbers is our way to do business. Is it yours too?
//           </motion.h2>

//           <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
//             <motion.div
//               className="text-center"
//               initial={{ opacity: 0, y: 20 }}
//               whileInView={{ opacity: 1, y: 0 }}
//               transition={{ duration: 0.6, delay: 0.1 }}
//               viewport={{ once: true }}
//             >
//               <div className="text-5xl md:text-6xl font-bold mb-4">25.5M+</div>
//               <div className="text-lg">Unique URLs checked<br />in over 11 years</div>
//             </motion.div>

//             <motion.div
//               className="text-center"
//               initial={{ opacity: 0, y: 20 }}
//               whileInView={{ opacity: 1, y: 0 }}
//               transition={{ duration: 0.6, delay: 0.2 }}
//               viewport={{ once: true }}
//             >
//               <div className="text-5xl md:text-6xl font-bold mb-4">85,000+</div>
//               <div className="text-lg">Happy customers<br />all over the world</div>
//             </motion.div>

//             <motion.div
//               className="text-center"
//               initial={{ opacity: 0, y: 20 }}
//               whileInView={{ opacity: 1, y: 0 }}
//               transition={{ duration: 0.6, delay: 0.3 }}
//               viewport={{ once: true }}
//             >
//               <div className="text-5xl md:text-6xl font-bold mb-4">120+</div>
//               <div className="text-lg">Countries served with<br />better SEO Services</div>
//             </motion.div>
//           </div>
//         </div>
//       </section>

//       {/* Testimonials Section */}
//       <section className="py-20 px-6 bg-gray-900">
//         <div className="max-w-7xl mx-auto">
//           <h2 className="text-4xl font-bold text-center text-white mb-16">
//             They use us to create great experiences
//           </h2>

//           <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
//             {[
//               {
//                 name: "Surrey",
//                 text: "I would like to start by saying I love your website and use it as a tool to better my work.",
//                 avatar: "👨‍💼"
//               },
//               {
//                 name: "Marco",
//                 text: "Thanks for your wonderful tool.",
//                 avatar: "👨‍💻"
//               },
//               {
//                 name: "Guy S.",
//                 text: "Excellent service and great support team!",
//                 avatar: "👨‍🎨"
//               }
//             ].map((testimonial, index) => (
//               <motion.div
//                 key={index}
//                 className="bg-gray-800/50 backdrop-blur-xl rounded-2xl p-6 shadow-lg border border-gray-700/50"
//                 initial={{ opacity: 0, y: 20 }}
//                 whileInView={{ opacity: 1, y: 0 }}
//                 transition={{ duration: 0.6, delay: index * 0.1 }}
//                 viewport={{ once: true }}
//               >
//                 <div className="flex items-center gap-3 mb-4">
//                   <div className="w-12 h-12 rounded-full bg-gradient-to-br from-green-400 to-blue-500 flex items-center justify-center text-2xl">
//                     {testimonial.avatar}
//                   </div>
//                   <div className="font-bold text-white">{testimonial.name}</div>
//                 </div>
//                 <p className="text-gray-300">{testimonial.text}</p>
//               </motion.div>
//             ))}
//           </div>
//         </div>
//       </section>

//       {/* Dashboard Preview Section */}
//       <section className="py-20 px-6 bg-gray-950">
//         <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
//           <motion.div
//             initial={{ opacity: 0, x: -50 }}
//             whileInView={{ opacity: 1, x: 0 }}
//             transition={{ duration: 0.6 }}
//             viewport={{ once: true }}
//           >
//             <p className="text-orange-500 font-semibold mb-2">Enjoy your Dashboard</p>
//             <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
//               Everything you need in one place
//             </h2>
//             <p className="text-gray-400 mb-6">
//               All of the tools right at your fingertips. With one quick click, you can see how your site is doing. The dashboard offers instant access to reports, monitors, and analysis tools.
//             </p>
//             <button
//               onClick={() => setActiveTab("dashboard")}
//               className="px-8 py-3 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
//             >
//               Start Free Trial
//             </button>
//           </motion.div>

//           <motion.div
//             className="relative"
//             initial={{ opacity: 0, x: 50 }}
//             whileInView={{ opacity: 1, x: 0 }}
//             transition={{ duration: 0.6 }}
//             viewport={{ once: true }}
//           >
//             <div className="bg-gray-900 rounded-lg shadow-2xl p-4 transform hover:scale-105 transition-transform duration-300">
//               <div className="bg-gradient-to-br from-orange-500 to-red-600 h-64 rounded flex items-center justify-center text-white text-6xl">
//                 📊
//               </div>
//             </div>
//           </motion.div>
//         </div>
//       </section>

//       {/* Features Grid Section */}
//       <section className="py-20 px-6 bg-gray-900">
//         <div className="max-w-7xl mx-auto">
//           <p className="text-center text-orange-500 font-semibold mb-2">Tons of great features</p>
//           <h2 className="text-4xl font-bold text-center text-white mb-16">
//             Introducing our SEO ToolBox
//           </h2>

//           <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
//             {[
//               {
//                 icon: "📈",
//                 title: "Instantly analyze your SEO issues",
//                 desc: "Run unlimited analysis on our most powerful servers. Stored reports make it easy to view progress and past work."
//               },
//               {
//                 icon: "🔄",
//                 title: "Professional SEO monitoring tools",
//                 desc: "Automatically keep track of weekly changes in more than 70 SEO variables. Get notifications if your SEO score changes."
//               },
//               {
//                 icon: "👥",
//                 title: "Understand your competitors' SEO profile",
//                 desc: "Side-by-side SEO comparisons of up to 5 competitors. See how your SEO can improve against the competition."
//               },
//               {
//                 icon: "📝",
//                 title: "Save hours with white-label SEO reports",
//                 desc: "Quickly create editable SEO reports for your clients or partner websites."
//               },
//               {
//                 icon: "💡",
//                 title: "SEO reports you can understand and act upon",
//                 desc: "SEO broken down in plain language, with clear definitions and 'how-to-fix' tutorials for each issue."
//               },
//               {
//                 icon: "🎁",
//                 title: "7-Day free trial, cancel anytime!",
//                 desc: "Get started right away by registering below. Plans start at $34.95 per month."
//               }
//             ].map((feature, index) => (
//               <motion.div
//                 key={index}
//                 className="bg-gray-800/50 backdrop-blur-xl rounded-2xl p-8 text-center hover:shadow-2xl transition-all duration-300 border border-gray-700/50 hover:border-orange-500/50"
//                 initial={{ opacity: 0, y: 20 }}
//                 whileInView={{ opacity: 1, y: 0 }}
//                 transition={{ duration: 0.6, delay: index * 0.1 }}
//                 viewport={{ once: true }}
//               >
//                 <div className="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-orange-500 to-red-600 rounded-full flex items-center justify-center text-3xl">
//                   {feature.icon}
//                 </div>
//                 <h3 className="text-xl font-bold text-white mb-3">
//                   {feature.title}
//                 </h3>
//                 <p className="text-gray-400 text-sm">
//                   {feature.desc}
//                 </p>
//               </motion.div>
//             ))}
//           </div>
//         </div>
//       </section>

//       {/* Final CTA Section */}
//       <section className="py-20 px-6 bg-gradient-to-r from-blue-900 to-blue-950 text-white">
//         <div className="max-w-4xl mx-auto text-center">
//           <h2 className="text-4xl md:text-5xl font-bold mb-8">
//             Check your website's SEO for free right now!
//           </h2>
//           <div className="flex flex-col sm:flex-row gap-4 justify-center max-w-3xl mx-auto">
//             <input
//               type="text"
//               placeholder="Website URL"
//               className="px-6 py-4 flex-1 rounded-lg text-gray-900 focus:outline-none focus:ring-4 focus:ring-orange-500"
//             />
//             <button
//               onClick={() => setActiveTab("analyzer")}
//               className="px-10 py-4 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
//             >
//               Checkup
//             </button>
//           </div>
//         </div>
//       </section>

//       {/* Footer */}
//       <footer className="bg-blue-950 text-white py-12 px-6">
//         <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
//           <div>
//             <div className="flex items-center gap-2 mb-4">
//               <div className="w-10 h-10 bg-orange-600 rounded flex items-center justify-center font-bold">
//                 S
//               </div>
//               <span className="font-bold text-lg">SEO Site Checkup</span>
//             </div>
//             <p className="text-sm text-gray-300 mb-4">
//               Website SEO, Monitoring & Automation Made Easy.
//             </p>
//             <div className="flex gap-3">
//               <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center hover:bg-gray-600 cursor-pointer transition">
//                 𝕏
//               </div>
//               <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center hover:bg-gray-600 cursor-pointer transition">
//                 f
//               </div>
//             </div>
//           </div>

//           <div>
//             <h3 className="font-bold mb-4">Product</h3>
//             <ul className="space-y-2 text-sm text-gray-300">
//               <li className="hover:text-white cursor-pointer">Pricing</li>
//               <li className="hover:text-white cursor-pointer">Free Tools</li>
//               <li className="hover:text-white cursor-pointer">Articles</li>
//               <li className="hover:text-white cursor-pointer">Login</li>
//               <li className="hover:text-white cursor-pointer">Free 7-Day Trial</li>
//             </ul>
//           </div>

//           <div>
//             <h3 className="font-bold mb-4">Company</h3>
//             <ul className="space-y-2 text-sm text-gray-300">
//               <li className="hover:text-white cursor-pointer">About us</li>
//               <li className="hover:text-white cursor-pointer">FAQs</li>
//               <li className="hover:text-white cursor-pointer">SEO Checkups</li>
//               <li className="hover:text-white cursor-pointer">Contact</li>
//             </ul>
//           </div>

//           <div>
//             <h3 className="font-bold mb-4">Legal</h3>
//             <ul className="space-y-2 text-sm text-gray-300">
//               <li className="hover:text-white cursor-pointer">Terms of Service</li>
//               <li className="hover:text-white cursor-pointer">Privacy Policy</li>
//               <li className="hover:text-white cursor-pointer">Refunds Policy</li>
//             </ul>
//           </div>
//         </div>

//         <div className="max-w-7xl mx-auto mt-12 pt-8 border-t border-gray-700 text-center text-sm text-gray-400">
//           © SEO Site Checkup 2020-2025 • All rights reserved
//         </div>
//       </footer>

//       {/* Floating Scroll to Top Button */}
//       <button
//         onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
//         className="fixed bottom-8 right-8 w-14 h-14 bg-orange-600 text-white rounded-full shadow-lg hover:bg-orange-700 transition flex items-center justify-center text-2xl z-50"
//       >
//         ↑
//       </button>
//     </div>
//   );
// }






import { motion } from "framer-motion";
import { useState } from "react";
import Galaxy from "./Galaxy";

export default function HomeLanding({ setActiveTab }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <div className="relative bg-gray-950 min-h-screen">
      {/* Hero Section with Galaxy Background */}
      <section className="relative min-h-screen flex flex-col overflow-hidden bg-gray-950">
        {/* Galaxy Background */}
        <div className="absolute inset-0 opacity-60">
          <Galaxy
            mouseRepulsion={true}
            mouseInteraction={true}
            density={1.2}
            glowIntensity={0.4}
            saturation={0.3}
            hueShift={200}
            rotationSpeed={0.05}
          />
        </div>

        {/* Header Navigation */}
        <motion.header
          className="relative z-20 pt-6 px-6"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <div className="max-w-7xl mx-auto">
            <nav className="flex items-center justify-between px-6 py-4 bg-gray-900/50 backdrop-blur-xl rounded-2xl border border-gray-800/50 shadow-2xl">
              {/* Logo */}
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-to-br from-orange-500 to-red-600 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold text-xl">S</span>
                </div>
                <span className="text-white font-bold text-xl">SEO Checkup</span>
              </div>

              {/* Desktop Navigation Links */}
              <div className="hidden lg:flex items-center gap-6">
                <button 
                  onClick={() => setActiveTab("home")}
                  className="text-gray-300 hover:text-white transition-colors font-medium"
                >
                  Home
                </button>
                <button 
                  onClick={() => setActiveTab("dashboard")}
                  className="text-gray-300 hover:text-white transition-colors font-medium"
                >
                  Dashboard
                </button>
                <button 
                  onClick={() => setActiveTab("analyzer")}
                  className="text-gray-300 hover:text-white transition-colors font-medium"
                >
                  Analyzer
                </button>
                <button className="text-gray-300 hover:text-white transition-colors font-medium">
                  AI Writer
                </button>
                <button className="text-gray-300 hover:text-white transition-colors font-medium">
                  Predict Performance
                </button>
                <button className="text-gray-300 hover:text-white transition-colors font-medium">
                  Competitor Insights
                </button>
              </div>

              {/* Right Side - Login & Mobile Menu */}
              <div className="flex items-center gap-4">
                {/* Login Button */}
                <button className="px-6 lg:px-8 py-2.5 bg-white text-gray-900 font-semibold rounded-full hover:bg-gray-100 transition shadow-lg">
                  Login
                </button>

                {/* Mobile Menu Button */}
                <button
                  onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                  className="lg:hidden text-white p-2"
                >
                  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    {mobileMenuOpen ? (
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    ) : (
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                    )}
                  </svg>
                </button>
              </div>
            </nav>

            {/* Mobile Menu Dropdown */}
            {mobileMenuOpen && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="lg:hidden mt-4 p-4 bg-gray-900/50 backdrop-blur-xl rounded-2xl border border-gray-800/50 shadow-2xl"
              >
                <div className="flex flex-col gap-3">
                  <button 
                    onClick={() => { setActiveTab("home"); setMobileMenuOpen(false); }}
                    className="text-left text-gray-300 hover:text-white transition-colors font-medium py-2"
                  >
                    Home
                  </button>
                  <button 
                    onClick={() => { setActiveTab("dashboard"); setMobileMenuOpen(false); }}
                    className="text-left text-gray-300 hover:text-white transition-colors font-medium py-2"
                  >
                    Dashboard
                  </button>
                  <button 
                    onClick={() => { setActiveTab("analyzer"); setMobileMenuOpen(false); }}
                    className="text-left text-gray-300 hover:text-white transition-colors font-medium py-2"
                  >
                    Analyzer
                  </button>
                  <button className="text-left text-gray-300 hover:text-white transition-colors font-medium py-2">
                    AI Writer
                  </button>
                  <button className="text-left text-gray-300 hover:text-white transition-colors font-medium py-2">
                    Predict Performance
                  </button>
                  <button className="text-left text-gray-300 hover:text-white transition-colors font-medium py-2">
                    Competitor Insights
                  </button>
                </div>
              </motion.div>
            )}
          </div>
        </motion.header>

        {/* Hero Content */}
        <div className="relative z-10 flex-1 flex flex-col items-center justify-center text-center px-6 py-20">
          {/* Badge */}
          <motion.div
            className="inline-flex items-center gap-2 px-4 py-2 bg-gray-900/50 backdrop-blur-xl rounded-full border border-gray-800/50 mb-8"
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <div className="w-5 h-5 flex items-center justify-center">
              <div className="w-3 h-3 bg-gradient-to-br from-orange-500 to-red-600 rounded"></div>
            </div>
            <span className="text-gray-300 text-sm font-medium">New SEO Analysis</span>
          </motion.div>

          {/* Main Heading */}
          <motion.h1
            className="text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-8 leading-tight max-w-5xl"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.3 }}
          >
            Analyze your website's SEO performance for free!
          </motion.h1>

          <motion.p
            className="text-xl text-gray-400 mb-12 max-w-2xl"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            Get a complete SEO report and discover how to improve your website's visibility
          </motion.p>

          {/* CTA Buttons */}
          <motion.div
            className="flex flex-col sm:flex-row items-center gap-4"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.5 }}
          >
            <button
              onClick={() => setActiveTab("analyzer")}
              className="px-8 py-4 bg-white text-gray-900 font-semibold rounded-full hover:bg-gray-100 transition shadow-xl hover:shadow-2xl hover:scale-105 transform duration-300"
            >
              Get Started
            </button>
            <button className="px-8 py-4 bg-transparent text-white font-semibold rounded-full border-2 border-gray-700 hover:border-gray-500 transition hover:bg-gray-900/30">
              Learn More
            </button>
          </motion.div>
        </div>
      </section>

      {/* Benefits Section with Illustration */}
      <section className="py-20 px-6 bg-gray-950">
        <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
          {/* Illustration */}
          <motion.div
            className="relative"
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <div className="relative w-full aspect-square">
              <div className="absolute inset-0 bg-gradient-to-br from-orange-400 to-orange-600 rounded-full opacity-90"></div>
              {/* <div className="absolute inset-0 flex items-center justify-center">
                <div className="text-white text-6xl">🚀</div>
              </div> */}
              <div className="absolute inset-0 flex items-center justify-center">
 
  <motion.img
    src="/robo.png"
    alt="SEO Robot"
    className="w-140 h-140 object-contain drop-shadow-[0_0_25px_#f97316]"
    animate={{
      rotate: [0, 5, -5, 0],
      y: [0, -10, 0],
      scale: [1, 1.05, 1],
      filter: [
        "drop-shadow(0 0 15px #fb923c)",
        "drop-shadow(0 0 25px #f97316)",
        "drop-shadow(0 0 15px #fb923c)",
      ],
    }}
    transition={{
      duration: 6,
      repeat: Infinity,
      ease: "easeInOut",
    }}
    whileHover={{
      rotate: 10,
      scale: 1.1,
      filter: "drop-shadow(0 0 40px #fb923c)",
    }}
  />
</div>


            </div>
          </motion.div>

          {/* Benefits Text */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Everything you need to uplift your business
            </h2>
            
            <div className="space-y-6">
              <div>
                <h3 className="text-xl font-bold text-white mb-2">
                  SEO doesn't need to be difficult
                </h3>
                <p className="text-gray-400">
                  We provide a set of SEO tools to help you understand your website from a search engine's perspective.
                </p>
              </div>

              <div>
                <h3 className="text-xl font-bold text-white mb-2">
                  Know when to act and improve
                </h3>
                <p className="text-gray-400">
                  Our SEO reports also let you know of any problems or technical shortcomings in your website that may be hurting your search engine rankings.
                </p>
              </div>

              <div>
                <h3 className="text-xl font-bold text-white mb-2">
                  Dedicated team of SEO professionals
                </h3>
                <p className="text-gray-400">
                  We've seen how algorithms, penalties and SEO factors have evolved since the early days of search. As SEO professionals and site owners, we know first-hand where webmasters need to focus and spend their time.
                </p>
              </div>

              <button
                onClick={() => setActiveTab("analyzer")}
                className="mt-6 px-8 py-4 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
              >
                I'm Ready For A 7-Day Free Trial
              </button>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 px-6 bg-gradient-to-r from-blue-900 to-blue-950 text-white">
        <div className="max-w-7xl mx-auto">
          <motion.h2
            className="text-3xl md:text-4xl font-bold text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            Conveying trust by numbers is our way to do business. Is it yours too?
          </motion.h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
            <motion.div
              className="text-center"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.1 }}
              viewport={{ once: true }}
            >
              <div className="text-5xl md:text-6xl font-bold mb-4">25.5M+</div>
              <div className="text-lg">Unique URLs checked<br />in over 11 years</div>
            </motion.div>

            <motion.div
              className="text-center"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              viewport={{ once: true }}
            >
              <div className="text-5xl md:text-6xl font-bold mb-4">85,000+</div>
              <div className="text-lg">Happy customers<br />all over the world</div>
            </motion.div>

            <motion.div
              className="text-center"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.3 }}
              viewport={{ once: true }}
            >
              <div className="text-5xl md:text-6xl font-bold mb-4">120+</div>
              <div className="text-lg">Countries served with<br />better SEO Services</div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-20 px-6 bg-gray-900">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-center text-white mb-16">
            They use us to create great experiences
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                name: "Surrey",
                text: "I would like to start by saying I love your website and use it as a tool to better my work.",
                avatar: "👨‍💼"
              },
              {
                name: "Marco",
                text: "Thanks for your wonderful tool.",
                avatar: "👨‍💻"
              },
              {
                name: "Guy S.",
                text: "Excellent service and great support team!",
                avatar: "👨‍🎨"
              }
            ].map((testimonial, index) => (
              <motion.div
                key={index}
                className="bg-gray-800/50 backdrop-blur-xl rounded-2xl p-6 shadow-lg border border-gray-700/50"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                viewport={{ once: true }}
              >
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-12 h-12 rounded-full bg-gradient-to-br from-green-400 to-blue-500 flex items-center justify-center text-2xl">
                    {testimonial.avatar}
                  </div>
                  <div className="font-bold text-white">{testimonial.name}</div>
                </div>
                <p className="text-gray-300">{testimonial.text}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Dashboard Preview Section */}
      <section className="py-20 px-6 bg-gray-950">
        <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <p className="text-orange-500 font-semibold mb-2">Enjoy your Dashboard</p>
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Everything you need in one place
            </h2>
            <p className="text-gray-400 mb-6">
              All of the tools right at your fingertips. With one quick click, you can see how your site is doing. The dashboard offers instant access to reports, monitors, and analysis tools.
            </p>
            <button
              onClick={() => setActiveTab("dashboard")}
              className="px-8 py-3 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
            >
              Start Free Trial
            </button>
          </motion.div>

          <motion.div
            className="relative"
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <div className="bg-gray-900 rounded-lg shadow-2xl p-4 transform hover:scale-105 transition-transform duration-300">
              <div className="bg-gradient-to-br from-orange-500 to-red-600 h-64 rounded flex items-center justify-center text-white text-6xl">
                📊
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features Grid Section */}
      <section className="py-20 px-6 bg-gray-900">
        <div className="max-w-7xl mx-auto">
          <p className="text-center text-orange-500 font-semibold mb-2">Tons of great features</p>
          <h2 className="text-4xl font-bold text-center text-white mb-16">
            Introducing our SEO ToolBox
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                icon: "📈",
                title: "Instantly analyze your SEO issues",
                desc: "Run unlimited analysis on our most powerful servers. Stored reports make it easy to view progress and past work."
              },
              {
                icon: "🔄",
                title: "Professional SEO monitoring tools",
                desc: "Automatically keep track of weekly changes in more than 70 SEO variables. Get notifications if your SEO score changes."
              },
              {
                icon: "👥",
                title: "Understand your competitors' SEO profile",
                desc: "Side-by-side SEO comparisons of up to 5 competitors. See how your SEO can improve against the competition."
              },
              {
                icon: "📝",
                title: "Save hours with white-label SEO reports",
                desc: "Quickly create editable SEO reports for your clients or partner websites."
              },
              {
                icon: "💡",
                title: "SEO reports you can understand and act upon",
                desc: "SEO broken down in plain language, with clear definitions and 'how-to-fix' tutorials for each issue."
              },
              {
                icon: "🎁",
                title: "7-Day free trial, cancel anytime!",
                desc: "Get started right away by registering below. Plans start at $34.95 per month."
              }
            ].map((feature, index) => (
              <motion.div
                key={index}
                className="bg-gray-800/50 backdrop-blur-xl rounded-2xl p-8 text-center hover:shadow-2xl transition-all duration-300 border border-gray-700/50 hover:border-orange-500/50"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                viewport={{ once: true }}
              >
                <div className="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-orange-500 to-red-600 rounded-full flex items-center justify-center text-3xl">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-bold text-white mb-3">
                  {feature.title}
                </h3>
                <p className="text-gray-400 text-sm">
                  {feature.desc}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Final CTA Section */}
      <section className="py-20 px-6 bg-gradient-to-r from-blue-900 to-blue-950 text-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-8">
            Check your website's SEO for free right now!
          </h2>
          <div className="flex flex-col sm:flex-row gap-4 justify-center max-w-3xl mx-auto">
            <input
              type="text"
              placeholder="Website URL"
              className="px-6 py-4 flex-1 rounded-lg text-gray-900 focus:outline-none focus:ring-4 focus:ring-orange-500"
            />
            <button
              onClick={() => setActiveTab("analyzer")}
              className="px-10 py-4 bg-orange-600 text-white font-semibold rounded-lg hover:bg-orange-700 transition"
            >
              Checkup
            </button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-blue-950 text-white py-12 px-6">
        <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center gap-2 mb-4">
              <div className="w-10 h-10 bg-orange-600 rounded flex items-center justify-center font-bold">
                S
              </div>
              <span className="font-bold text-lg">SEO Site Checkup</span>
            </div>
            <p className="text-sm text-gray-300 mb-4">
              Website SEO, Monitoring & Automation Made Easy.
            </p>
            <div className="flex gap-3">
              <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center hover:bg-gray-600 cursor-pointer transition">
                𝕏
              </div>
              <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center hover:bg-gray-600 cursor-pointer transition">
                f
              </div>
            </div>
          </div>

          <div>
            <h3 className="font-bold mb-4">Product</h3>
            <ul className="space-y-2 text-sm text-gray-300">
              <li className="hover:text-white cursor-pointer">Pricing</li>
              <li className="hover:text-white cursor-pointer">Free Tools</li>
              <li className="hover:text-white cursor-pointer">Articles</li>
              <li className="hover:text-white cursor-pointer">Login</li>
              <li className="hover:text-white cursor-pointer">Free 7-Day Trial</li>
            </ul>
          </div>

          <div>
            <h3 className="font-bold mb-4">Company</h3>
            <ul className="space-y-2 text-sm text-gray-300">
              <li className="hover:text-white cursor-pointer">About us</li>
              <li className="hover:text-white cursor-pointer">FAQs</li>
              <li className="hover:text-white cursor-pointer">SEO Checkups</li>
              <li className="hover:text-white cursor-pointer">Contact</li>
            </ul>
          </div>

          <div>
            <h3 className="font-bold mb-4">Legal</h3>
            <ul className="space-y-2 text-sm text-gray-300">
              <li className="hover:text-white cursor-pointer">Terms of Service</li>
              <li className="hover:text-white cursor-pointer">Privacy Policy</li>
              <li className="hover:text-white cursor-pointer">Refunds Policy</li>
            </ul>
          </div>
        </div>

        <div className="max-w-7xl mx-auto mt-12 pt-8 border-t border-gray-700 text-center text-sm text-gray-400">
          © SEO Site Checkup 2020-2025 • All rights reserved
        </div>
      </footer>

      {/* Floating Scroll to Top Button */}
      <button
        onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
        className="fixed bottom-8 right-8 w-14 h-14 bg-orange-600 text-white rounded-full shadow-lg hover:bg-orange-700 transition flex items-center justify-center text-2xl z-50"
      >
        ↑
      </button>
    </div>
  );
}